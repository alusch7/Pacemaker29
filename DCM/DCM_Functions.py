import sys
import os
#This is the start of the functions for the DCM

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

