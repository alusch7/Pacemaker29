import sys
import os
#This is the start of the functions for the DCM
import serial
import struct
import serial.tools.list_ports

def test():
    return None

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
    values = []

    Signal_echo = Start + SYNC + FN_CODE + MODE + LRL + AtrialAMP + VentAMP + AtrPW + VentPW + AtrSens + VentSens + VRP + ARP
    i = 0

    with serial.Serial(FRDM_PORT, 115200) as pacemaker:
        pacemaker.write(Signal_echo)
        data = pacemaker.read(19)
        get_MODE = data[2]
        get_LRL = data[3]
        get_Atrial_AMP = struct.unpack("f", data[4:7])
        get_Vent_AMP = struct.unpack("f", data[8:11])
        get_Atrial_PW = data[12]
        get_Vent_PW = data[13]
        get_Atrial_Sens = data[14]
        get_Vent_Sens = data[15]
        get_VRP = struct.unpack("H", data[16:17])
        get_ARP = struct.unpack("H", data[18:19])
    
    values.append[get_LRL]
    values.append[get_Atrial_AMP]
    values.append[get_Atrial_PW]
    values.append[get_Vent_AMP]
    values.append[get_Vent_PW]
    values.append[get_Vent_Sens]
    values.append[get_Atrial_Sens]


    print(get_MODE)
    print(get_LRL)
    print(get_Atrial_AMP)
    print(get_Vent_AMP)
    print(get_Atrial_PW)
    print(get_Vent_PW)
    print(get_Atrial_Sens)
    print(get_Vent_Sens)
    print(get_VRP)
    print(get_ARP)

    #print("From the board")
    #print(M)
    #print(L)
    #print(AA)
    #print(VA)

def send_data():

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

    Signal_write = Start + FN_CODE + MODE + LRL + AtrialAMP + VentAMP + AtrPW + VentPW + AtrSens + VentSens + VRP + ARP
    i = 0

    with serial.Serial(FRDM_PORT, 115200) as pacemaker:
        pacemaker.write(Signal_write)

#recieve_data()

