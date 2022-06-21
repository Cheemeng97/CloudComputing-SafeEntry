from __future__ import print_function

import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

#import PySimpleGUI as sg

import datetime
import pandas as pd
#import history_windows
from tkinter import *

import ctypes
import sys
import random



localhost = 'localhost:50052'


'''
Module: Testing Check in
--------------------------------------------------------
name = Amanda
nric = 885A
location = Koufu
checkin time = 6/21/2022 12:31
groupid = None

To run on terminal 

python testing.py checkin name nric location checkin_time 

'''
import safeentry_client

successmessage = "Check data.csv to view entry. Ensure you close the file before carrying on. \nClick anywhere to carry on."
failuremessage = "Type Y or exit"


if __name__ == '__main__':
    now = datetime.datetime.now()
    checkin_dt = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print("-----Testing Proceedure ------------")
    print('1. Check in \n2. Check out \n3. Group Check in \n4. Group Check Out \n5. Admin \n6. History \n7. Notifications')
    print("\n\n\nScenario \nYou are Amanda (885A) checking into Koufu right now. You will be able to view a success pop up")
    safeentry_client.checkin("Amanda1","8852A","South",checkin_dt)
    input(successmessage)
    print("\n\n\nScenario \nYou are Amanda (885A) checking out of Koufu right now. You will be able to view a success pop up")
    safeentry_client.checkout("Amanda1","8852A","South",checkin_dt)
    input(successmessage)
    print("\n\n\nScenario \nYou are Amanda (885A) checking out of Foodgle right now. You will be able to view a fail pop up")
    safeentry_client.checkout("Amanda1","8852A","Foodgle",checkin_dt)
    input(successmessage)
    print("\n\n\nScenario \nYou are logging in your family member Tim (887A) into South Canteen with you.You should see 2 success pop up.")
    group_info = [["Amanda","8852A"],["Tim","887A"]]
    safeentry_client.group_checkin(group_info,"Foodgle",checkin_dt)
    print("\n\n\nScenario \nYou are checking out your family member Tim (887A) from South Canteen with you.You should see 2 success pop up.")
    group_info = [["Amanda","8852A"],["Tim","887A"]]
    safeentry_client.checkout("Amanda1","8852A","Foodgle",checkin_dt)
    print("\n\n\nScenario \nYou are Unknown (000x) viewing your checkin/out history. You will wont be able to view checkin/out history records in terminal")
    safeentry_client.history("000x")
    print("No records")
    input(successmessage)
    print("\n\n\nScenario \nYou are Amanda (885A) viewing your checkin/out history. You will be able to view the checkin/out history records in terminal")
    safeentry_client.history("8852A")
    input(successmessage)
    print("\n\n\nScenario \nYou are Amanda (885A) viewing your possible exposure notification. You should see the affected notification pop up")
    safeentry_client.check("8852A")
    input(successmessage)
    







    #function_call = "safeentry_client." + sys.argv[1]

    #checkin(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]+" " +sys.argv[6])
