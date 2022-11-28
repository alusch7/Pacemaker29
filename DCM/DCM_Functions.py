import sys
import os
import time
#This is the start of the functions for the DCM
import serial
import struct
import serial.tools.list_ports

# Port for specific computer
#FRDM_PORT = '/dev/cu.usbmodem1444203'
FRDM_PORT = 'COM4'

def is_connected():
    try:
        with serial.Serial(FRDM_PORT, 115200) as pacemaker:
            pacemaker.close()
        return True
    except:
        return False
    return False


def UART_receive_data():

    
    SYNC = b'\x22'  # This is only for recieving data from Simulink
    Start = b'\x16'
    FN_CODE = b'\x55'   # This is only for sending data to Simulink
    MODE = struct.pack("B", 1) #For VOO
    LRL = struct.pack("B", 1) 
    AtrialAMP = struct.pack("f", 0.5)
    VentAMP = struct.pack("f", 2.6)
    AtrPW = struct.pack("B", 1)
    VentPW = struct.pack("B", 1)
    AtrSens = struct.pack("B", 1)
    VentSens = struct.pack("B", 1)
    VRP = struct.pack("H", 10) #Unsigned Short Size 2
    ARP = struct.pack("H", 10)
    VentSignal = struct.pack("f", 0)
    AtrSignal = struct.pack("f", 0)
    values = []

    
    Signal_echo = Start + SYNC + MODE + LRL + AtrialAMP + VentAMP + AtrPW + VentPW + AtrSens + VentSens + VRP + ARP + VentSignal + AtrSignal
    data_received = False
    # print("Starting data receive...")
    while ~data_received:
        try:
            with serial.Serial(FRDM_PORT, 115200) as pacemaker:
                pacemaker.write(Signal_echo)
                # time.sleep(0.001)
                data = pacemaker.read(26)
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
                get_VentSignal = struct.unpack("f", data[18:22])[0]
                get_AtrSignal = struct.unpack("f", data[22:26])[0]
                data_received = True
                # print("Data received!")
                pacemaker.close()
                break
        except:
            print("Error detected.. restarting")
            data_received = False
    
    values.append(get_LRL)
    values.append(get_Atrial_AMP)
    values.append(get_Atrial_PW)
    values.append(get_Vent_AMP)
    values.append(get_Vent_PW)
    values.append(get_Vent_Sens)
    values.append(get_Atrial_Sens)
    values.append(get_VentSignal)
    values.append(get_AtrSignal)
    
    # Debugging Print Statements
##    print(get_MODE)
##    print(get_LRL)
##    print(get_Atrial_AMP)
##    print(get_Vent_AMP)
##    print(get_Atrial_PW)
##    print(get_Vent_PW)
##    print(get_Atrial_Sens)
##    print(get_Vent_Sens)
##    print(get_VRP)
##    print(get_ARP)
##    print(get_VentSignal)
##    print(get_AtrSignal)

    return values
    

def UART_send_data(out_data):
    SYNC = b'\x22'
    Start = b'\x16'
    FN_CODE = b'\x55'
    MODE = struct.pack("B", out_data[0])
    LRL = struct.pack("B", out_data[1]) 
    AtrialAMP = struct.pack("f", out_data[2])
    VentAMP = struct.pack("f", out_data[3])
    AtrPW = struct.pack("B", out_data[4])
    VentPW = struct.pack("B", out_data[5])
    AtrSens = struct.pack("B", out_data[6])
    VentSens = struct.pack("B", out_data[7])
    VRP = struct.pack("H", out_data[8]) #Unsigned Short Size 2
    ARP = struct.pack("H", out_data[9])
    VentSignal = struct.pack("f", 0.0)
    AtrSignal = struct.pack("f", 0.0)


    Signal_write = Start + FN_CODE + MODE + LRL + AtrialAMP + VentAMP + AtrPW + VentPW + AtrSens + VentSens + VRP + ARP + VentSignal + AtrSignal
    print("Starting data send...")
    with serial.Serial(FRDM_PORT, 115200) as pacemaker:
        pacemaker.write(Signal_write)
        pacemaker.close()
    print("Data sent!")


