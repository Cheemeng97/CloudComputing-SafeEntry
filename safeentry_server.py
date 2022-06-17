# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc
import pandas as pd
import datetime


class Safeentry(safeentry_pb2_grpc.SafeEntryServiceServicer):

    def Checkin(self, request, context):

        #if failed to check in, return error message
        try:
            #add request data into pandas dataframe
            df = pd.DataFrame(columns=['name', 'nric', 'location', 'checkin_dt','checkout_dt','affected'])
            df.loc[0] = [request.name, request.nric, request.location, request.datetime, None,None]
            
            #write dataframe to csv file
            df.to_csv('./data.csv', mode='a', index=False, header=False)
            return safeentry_pb2.CheckIn_Reply(message='\n Check in successful   ' + 'name: ' + request.name + '   nric: ' + request.nric + '   location: ' + request.location+ '   datetime: ' + request.datetime)
        except:
            return safeentry_pb2.CheckIn_Reply(message='\n Check in failed')

    def Checkout(self, request, context):

        try:
            current_records = pd.read_csv('data.csv')
            #print(current_records)
            checkedin_records = current_records[current_records['checkout_dt'].isnull()]
            checkedout_records = current_records[current_records['checkout_dt'].notnull()]
            #print(checkedin_records)

            #filter by user 
            try:
                #print(checkedin_records[checkedin_records.loc[checkedin_records['nric'] == request.nric & checkedin_records['location'] == request.location]])
                checkedin_records['checkout_dt']= (checkedin_records.loc[checkedin_records['nric'] == request.nric])['checkout_dt'].fillna(request.datetime)
                #print('break')
                updated_records = checkedout_records.append(checkedin_records, ignore_index=True)
                #print(updated_records)
                #updated_records
                updated_records.to_csv('./data.csv', index=False)

            except:
                print("you have not checked in")

            return safeentry_pb2.Reply(message='\n Check out successful   ' + 'name: ' + request.name + '   nric: ' + request.nric + '   location: ' + request.location+ '   datetime: ' + request.datetime)
        except:
            return safeentry_pb2.Reply(message='\n Check Out failed')
        

    def Contacted(self, request, context):
        current_records = pd.read_csv('data.csv')
        affectedrecords = current_records.loc[current_records['location'] == request.location]
        #unaffectedrecords = current_records['location']!=request.location
        affecteddate = datetime.datetime.strptime(request.datetime, "%m/%d/%Y %H:%M")
        affectedrecords['checkin_dt'] =affectedrecords['checkin_dt'].astype("str")
        startdate = datetime.datetime.strptime(affectedrecords['checkin_dt'], "%m/%d/%Y %H:%M")
        enddate = datetime.datetime.strptime(affectedrecords['checkout_dt'].astype("str"), "%m/%d/%Y %H:%M")
        print(affectedrecords)
        affectedrecords['checkout_dt']= (affectedrecords.loc[startdate <= affecteddate <= enddate])['checkout_dt'].fillna("Y")
        print(affectedrecords)

        return safeentry_pb2.Reply(message='name: ' + request.name + '\nnric: ' + request.nric + '\nlocation: ' + request.location+ '\ndatetime: ' + request.datetime+ '\n Check Out successful')

    def History(self, request, context):
        #read data from csv file and add into dataframe
        df = pd.read_csv('./data.csv')
        nric = request.nric

        #filter dataframe by nric
        df = df[df['nric'] == nric]
        
        #convert all data to string
        df['name'] = df['name'].astype(str)
        df['nric'] = df['nric'].astype(str)
        df['location'] = df['location'].astype(str)
        df['checkin_dt'] = df['checkin_dt'].astype(str)
        df['checkout_dt'] = df['checkout_dt'].astype(str)

        data = []
        for index, row in df.iterrows():
            data.append((safeentry_pb2.History_Item(name=row['name'], nric=row['nric'], location=row['location'], checkin_dt=row['checkin_dt'], checkout_dt=row['checkout_dt'])))

        print(data)
            
        #return data array
        return safeentry_pb2.History_Reply(histories=data)

            

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServiceServicer_to_server(Safeentry(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
