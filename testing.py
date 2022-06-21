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
from safeentry_client import checkin


if __name__ == '__main__':
    function_call = "safeentry_client." + sys.argv[1]
    checkin(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]+" " +sys.argv[6])
