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

def checkin(name, nric, location, checkin_dt):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = safeentry_pb2_grpc.SafeEntryServiceStub(channel)
        response = stub.Checkin(safeentry_pb2.CheckIn_Request(name=name, nric=nric, location=location, datetime=checkin_dt))
        #print("Check In Status ===" + str(response))


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

#History tab
history_layout = [[sg.Text('History', background_color='tan1')],
               [sg.Input(key='-in2-')]]

#Notification tab
notification_layout = [[sg.Text('Notification', background_color='tan1')],
               [sg.Input(key='-in2-')]]


# tab group
tab_layout = [[sg.TabGroup([[
    sg.Tab('Check In', checkin_layout), 
    sg.Tab('History', history_layout),
    sg.Tab('Notification', notification_layout)]])]]

# Create the window
window = sg.Window("Safe Entry", tab_layout)

# Create an event loop
while True:
    event, values = window.read()
    print(values)

    place = ""
    if values['-place1-']:
        place = "Koufu"
    elif values['-place2-']:
        place = "Foodgle"
    elif values['-place3-']:
        place = "South Canteen"
    elif values['-place4-']:
        place = "North Canteen"

    # End program if user closes window 
    if event == sg.WIN_CLOSED:
        break

    if event == "Checkin":
        logging.basicConfig()
        checkin("client 1", "990Z", place, "2018-01-01T00:00:00Z")
        print("checkin successful")

    if event == "Checkout":
        print("checkout")

# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
