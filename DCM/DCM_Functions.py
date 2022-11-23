import sys
import os
#This is the start of the functions for the DCM
import serial
import struct
import serial.tools.list_ports

def test():
    return "a"

def get_connection_string(pacemaker_connected):
    if(pacemaker_connected):
        connection_string = "Connected"
    else:
        connection_string = "Disconnected"
    return connection_string

def get_connection_color(pacemaker_connected):
    if(pacemaker_connected):
        connection_colour = "Green"
    else:
        connection_colour = "red"
    return connection_colour

def recieve_data():

    FRDM_PORT = '/dev/cu.usbmodem1444203'
    SYNC = b'\x22'
    Start = b'\x16'
    FN_CODE = b'\x55'
    MODE = struct.pack("B", 1) #For VOO
    LRL = struct.pack("B", 1) 
    AtrialAMP = struct.pack("f", 1000)
    VentAMP = struct.pack("f", 1000)
    AtrPW = struct.pack("B", 1)
    VentPW = struct.pack("B", 1)
    AtrSens = struct.pack("B", 1)
    VentSens = struct.pack("B", 1)
    VRP = struct.pack("H", 10) #Unsigned Short Size 2
    ARP = struct.pack("H", 10)

    Signal_echo = Start + SYNC + FN_CODE + MODE + LRL + AtrialAMP + VentAMP + AtrPW + VentPW + AtrSens + VentSens + VRP + ARP
    i = 0

    with serial.Serial(FRDM_PORT, 115200) as pacemaker:
        pacemaker.write(Signal_echo)
        data = pacemaker.read(18)
        M = data[0]
        L = data[1]
        while (i < 18):
            print(data[i])
            i=i+1;
        #AA = struct.unpack("f", data[5:8])
        #VA = struct.unpack("f", data[9:12])

    #print("From the board")
    #print(M)
    #print(L)
    #print(AA)
    #print(VA)

recieve_data()