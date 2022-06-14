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


class Safeentry(safeentry_pb2_grpc.SafeEntryServiceServicer):

   def Checkin(self, request, context):

        #add request data into pandas dataframe
        df = pd.DataFrame(columns=['name', 'nric', 'location', 'checkin_dt','checkout_dt'])
        df.loc[0] = [request.name, request.nric, request.location, request.datetime, None]
        
        #write dataframe to csv file
        df.to_csv('./data.csv', mode='a', index=False, header=False)
        return safeentry_pb2.CheckIn_Reply(message='name: ' + request.name + '\nnric: ' + request.nric + '\nlocation: ' + request.location+ '\ndatetime: ' + request.datetime+ '\n Check in successful')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServiceServicer_to_server(Safeentry(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
