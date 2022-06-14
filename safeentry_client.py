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

def checkin(name, nric, location, checkin_dt):
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.Checkin(safeentry_pb2.CheckIn_Request(name=name, nric=nric, location=location, datetime=checkin_dt))
        #print("Check In Status ===" + str(response))

def checkout(name, nric, location, checkout_dt):
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.Checkout(safeentry_pb2.Request(name=name, nric=nric, location=location, datetime=checkout_dt))
        #print("Check In Status ===" + str(response))



#Log in tab
login_layout = [[sg.Text('NRIC', background_color='tan1')],
               [sg.Input(key='-nric_in-')]
               ,[sg.Text('Name', background_color='tan1')],
                [sg.Input(key='-name_in-')]
                ,[sg.Button("Login")]
               ]

#Check in out tab
checkin_layout = [[
    sg.Text("SafeEntry Check In")], 
    [sg.Radio('Koufu', 'place', default=True, key='-place1-') ,
           sg.Radio('Foodgle', 'place', key='-place2-')
           ,sg.Radio('South Canteen', 'place', key='-place3-')
           ,sg.Radio('North Canteen', 'place', key='-place4-')],
    [sg.Button("Checkin")], 
    [sg.Button("Checkout")]
    ]

#History tab with table
# history_layout = [[sg.Text("History")],
#                     [sg.Table(values=[['', '', '', '', '']],
#                                 headings=['Name', 'NRIC', 'Location', 'Check In', 'Check Out'],
#                                 auto_size_cells=False,
#                                 display_row_numbers=True,
#                                 num_rows=10,
#                                 row_height=35,
#                                 alternating_row_color='lightblue',
#                                 key='-table-')],
#                     [sg.Button("Refresh")]
#                     ]
history_layout = [[sg.Text('History', background_color='tan1')],
               [sg.Input(key='-in2-')]]

#Notification tab
notification_layout = [[sg.Text('Notification', background_color='tan1')],
               [sg.Input(key='-in2-')]]

admin_layout = [[sg.Text('Location', background_color='tan1')],
               [sg.Input(key='-closecontact_location-')]
               ,[sg.Text('DateTime', background_color='tan1')],
                [sg.Input(key='-closecontact_time-')]
                ,[sg.Button("Notify")]
               ]


# tab group
tab_layout = [[sg.TabGroup([[
    sg.Tab('Check In', checkin_layout), 
    sg.Tab('History', history_layout),
    sg.Tab('Notification', notification_layout)]])]] 

# Create the window
# window = sg.Window("Safe Entry", tab_layout)
loginwindow = sg.Window("Login", login_layout)
window = sg.Window("Safe Entry", tab_layout)
adminwindow = sg.Window("Admin",admin_layout)

nric = ''
name = ''

# Create an event loop
while True:
    login_event, login_values = loginwindow.read()
    print(login_event, login_values)

    if login_event == 'Login':
        nric = login_values['-nric_in-']
        name = login_values['-name_in-']
        loginwindow.close()
        window
    
    if name == "admin":
        admin_event, admin_values = adminwindow.read()
        print(admin_event, admin_values)

        # End program if user closes window 
        if event == sg.WIN_CLOSED:
            break

        if event == "Notify":
            
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

# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
