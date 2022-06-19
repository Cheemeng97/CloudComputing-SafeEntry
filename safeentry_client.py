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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

import PySimpleGUI as sg

import datetime
import pandas as pd
import history_windows
from tkinter import *

import ctypes

sg.theme('DarkBlue13')

localhost = 'localhost:50052'

def checkin(name, nric, location, checkin_dt):
    with grpc.insecure_channel(localhost) as channel:

        
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.Checkin(safeentry_pb2.CheckIn_Request(name=name, nric=nric, location=location, datetime=checkin_dt))
        ctypes.windll.user32.MessageBoxW(0, str(response.message), "Check In Status", 0)

def checkout(name, nric, location, checkout_dt):
    with grpc.insecure_channel(localhost) as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.Checkout(safeentry_pb2.Request(name=name, nric=nric, location=location, datetime=checkout_dt))
        ctypes.windll.user32.MessageBoxW(0, str(response.message), "Check Out Status", 0)

def contact(name, nric, location, checkout_dt):
    with grpc.insecure_channel(localhost) as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.Contacted(safeentry_pb2.Request(name=name, nric=nric, location=location, datetime=checkout_dt))
        #print("Check In Status ===" + str(response))


def check(nric):
    with grpc.insecure_channel(localhost) as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.checkContacted(safeentry_pb2.Check_Request(nric=nric))
        check_df = pd.DataFrame(columns=['name', 'nric', 'location', 'checkin_dt','checkout_dt'])

        for i in range(len(response.checks)):
            check_df.loc[i] = [response.checks[i].name, response.checks[i].nric, response.checks[i].location, response.checks[i].checkin_dt, response.checks[i].checkout_dt]
        
        check_df = check_df.sort_values(by='checkin_dt', ascending=False)

        for i in range(len(check_df)):
                location = check_df.iloc[i]['location']
                checkin_dt = check_df.iloc[i]['checkin_dt']
                checkout_dt = check_df.iloc[i]['checkout_dt']

                #get date only
                date = checkin_dt[:10]
                contactedmessage = "You are affected at " + str(location) + " on " + str(date) + ".    checkin_dt: " + str(checkin_dt) + " checkout_dt: " + str(checkout_dt)
                ctypes.windll.user32.MessageBoxW(0, str(contactedmessage), "Contacted Status", 0)

        
        

# #global variable for history
histories = []
def history(nric):
    with grpc.insecure_channel(localhost) as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.History(safeentry_pb2.History_Request(nric=nric))
        #put response data into dataframe
        history_df = pd.DataFrame(columns=['name', 'nric', 'location', 'checkin_dt','checkout_dt'])

        

        for i in range(len(response.histories)):
            history_df.loc[i] = [response.histories[i].name, response.histories[i].nric, response.histories[i].location, response.histories[i].checkin_dt, response.histories[i].checkout_dt]


        history_df = history_df.sort_values(by='checkin_dt', ascending=False)
               
        for i in range(len(history_df)):
            histories.append([history_df.iloc[i]['name'], history_df.iloc[i]['nric'], history_df.iloc[i]['location'], history_df.iloc[i]['checkin_dt'], history_df.iloc[i]['checkout_dt']])
            
        print(histories)


#Log in tab
login_layout = [[sg.Text('NRIC')],
               [sg.Input(key='-nric_in-')]
               ,[sg.Text('Name')],
                [sg.Input(key='-name_in-')]
                ,[sg.Button("Login")]
               ]

#Check in out tab
main_layout = [
    [sg.Text("SafeEntry Check In")], 
    [sg.Radio('Koufu', 'place', default=True, key='-place1-') ,
           sg.Radio('Foodgle', 'place', key='-place2-')
           ,sg.Radio('South Canteen', 'place', key='-place3-')
           ,sg.Radio('North Canteen', 'place', key='-place4-')],
    [sg.Button("Checkin"), sg.Button("Checkout")], 
    [sg.Text("")], 
    [sg.Button('Show Histories')],
    ]

centered_main_layout = [[sg.VPush()],
              [sg.Push(), sg.Column(main_layout,element_justification='c'), sg.Push()],
              [sg.VPush()]]

#Group check in out tab
group_checkin_layout = [[sg.Text("SafeEntry Group Check In")],
            [sg.Text('NRIC', background_color='tan1')], 
            [sg.Input(key='-group_nric_in-')],
            
            [sg.Text('Name', background_color='tan1')],
            [sg.Input(key='-group_name_in-')],
            
            [sg.Button("Add people")],

            [sg.Radio('Koufu', 'place', default=True, key='-group_place1-') ,
            sg.Radio('Foodgle', 'place', key='-group_place2-'),
            sg.Radio('South Canteen', 'place', key='-group_place3-'),
            sg.Radio('North Canteen', 'place', key='-group_place4-')], 
                
            [sg.Button("Group Checkin")]
           ]

admin_layout = [[sg.Text('Location', background_color='tan1')],
               [sg.Input(key='-closecontact_location-')]
               ,[sg.Text('DateTime', background_color='tan1')],
                [sg.Input(key='-closecontact_time-')]
                ,[sg.Button("Notify")]
               ]

# tab group
tab_layout = [[sg.TabGroup([[
    sg.Tab('Main Page', centered_main_layout)]])]] 

# Create the window
# window = sg.Window("Safe Entry", tab_layout)
loginwindow = sg.Window("Login", login_layout)
window = sg.Window("Safe Entry", tab_layout,grab_anywhere=True,)
adminwindow = sg.Window("Admin",admin_layout)

nric = ''
name = ''
# Create an event loop
while True:
    login_event, login_values = loginwindow.read()
    #print(login_event, login_values)

    if login_event == 'Login':
        nric = login_values['-nric_in-']
        name = login_values['-name_in-']
        loginwindow.close()
        window
        if name != 'admin':
            check(nric)


    if name == "admin":
        admin_event, admin_values = adminwindow.read()
        print(admin_event, admin_values)
        
        # End program if user closes window 
        if admin_event == sg.WIN_CLOSED:
            break

        if admin_event == "Notify":
            location = admin_values['-closecontact_location-']
            dateandtime = admin_values['-closecontact_time-']
            contact(None, None, location, dateandtime)
            print("Notify Success")

    else:
        
        event, values = window.read()
        print(event, values)

       
        place = "Koufu"
        if values['-place1-']:
            place = "Koufu"
        elif values['-place2-']:
            place = "Foodgle"
        elif values['-place3-']:
            place = "South Canteen"
        elif values['-place4-']:
            place = "North Canteen"
        else:
            place = "Koufu"

        now = datetime.datetime.now()
        checkin_dt = now.strftime("%Y-%m-%d %H:%M:%S")

        # End program if user closes window 
        if event == sg.WIN_CLOSED:
            break

        if event == "Checkin":
            logging.basicConfig()
            checkin(name, nric, place, checkin_dt)
            print("CHECKIN successful")

        if event == "Checkout":
            checkout(name, nric, place, checkin_dt)
            print("CHECKOUT successful")
       
        # End program if user closes window 
        if event == sg.WIN_CLOSED:
            break

        if event == 'Show Histories':
            histories = []
            history(nric)
            history_windows.create(histories)

        if event == "Checkout":
            print("CHECKOUT successful")

        if event == "Group Checkin":
            logging.basicConfig()
            #groupcheckin(name, nric, place, checkin_dt)
            print("GROUP CHECKIN successful")

        if event == "Add people":
            print("ADD PEOPLE successful")

# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
