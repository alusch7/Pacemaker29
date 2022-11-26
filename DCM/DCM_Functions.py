import sys
import os
#This is the start of the functions for the DCM
import serial
import struct
import serial.tools.list_ports

def test():
    return None

def receive_data():

    # FRDM_PORT = '/dev/cu.usbmodem1444203'
    FRDM_PORT = 'COM4'
    SYNC = b'\x22'      # This is only for recieving data from Simulink
    Start = b'\x16'
    FN_CODE = b'\x55'   # This is only for sending data to Simulink
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
    #VentSignal = struct.pack("f", 1000) #Unsigned Short Size 2
    #AtrSignal = struct.pack("f", 1000)
    values = []

    Signal_echo = Start + SYNC + MODE + LRL + AtrialAMP + VentAMP + AtrPW + VentPW + AtrSens + VentSens + VRP + ARP #  + VentSignal + AtrSignal
    i = 0

    with serial.Serial(FRDM_PORT, 115200, timeout = 1) as pacemaker:
        print("Starting read...")
        pacemaker.write(Signal_echo)
        print("Write Done...")
        data = pacemaker.read(18)
        print(data)
        print("Data Ready.")
        get_MODE = data[0]
        get_LRL = data[1]
        get_Atrial_AMP = struct.unpack("f", data[2:6])[0]
        get_Vent_AMP = struct.unpack("f", data[6:10])[0]
        get_Atrial_PW = data[10]
        get_Vent_PW = data[11]
        get_Atrial_Sens = data[12]
        get_Vent_Sens = data[13]
        get_VRP = struct.unpack("H", data[14:16])[0]
        get_ARP = struct.unpack("H", data[16:18])[0]
        # get_VentSignal = struct.unpack("f", data[20:23])
        # get_AtrSignal = struct.unpack("f", data[24:27])
        
    
    values.append(get_LRL)
    values.append(get_Atrial_AMP)
    values.append(get_Atrial_PW)
    values.append(get_Vent_AMP)
    values.append(get_Vent_PW)
    values.append(get_Vent_Sens)
    values.append(get_Atrial_Sens)


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

# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p)

# receive_data()
