# -*- coding: utf-8 -*-

import PySimpleGUI as sg

#sg.Window(title="Hello World", layout=[[]], margins=(1000, 1000)).read()

import PySimpleGUI as sg
def welcome_screen():
    layout1 = [
                [sg.Text("Welcome Page", justification='center')], 
                [sg.Button("Register New User",size=(10,2))], 
                [sg.Button("Login As Existing User",size=(10,2))]
                
              ]

    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    while True:
        event, values = window1.read()
        # End program if user closes window or
        # presses the OK button
        flag = 0
        if (event == "Register New User"):
            flag = 1
            break
        elif(event == "Login As Existing User"):
            flag = 2
            break
        elif (event == sg.WIN_CLOSED):
            break
    window1.close()
    
    if(flag == 1):
        registry()
    elif(flag == 2):
        login()
        
def registry():
    layout1 = [
                [sg.Text("Register New User", justification='center')]
               # [sg.Button("Register New User",size=(10,2))], 
                #[sg.Button("Login As Existing User",size=(10,2))]
                
              ]

    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    while True:
        event, values = window1.read()
        # End program if user closes window or
        # presses the OK button
        flag = 0
        if (event == "Register New User"):
            flag = 1
            break
        elif(event == "Login As Existing User"):
            flag = 2
            break
        elif (event == sg.WIN_CLOSED):
            break
    window1.close()
    
def login():
    layout1 = [
                [sg.Text("Login", justification='center')]
               # [sg.Button("Register New User",size=(10,2))], 
                #[sg.Button("Login As Existing User",size=(10,2))]
                
              ]

    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    while True:
        event, values = window1.read()
        # End program if user closes window or
        # presses the OK button
        flag = 0
        if (event == "Register New User"):
            flag = 1
            break
        elif(event == "Login As Existing User"):
            flag = 2
            break
        elif (event == sg.WIN_CLOSED):
            break
    window1.close()     

    
sg.theme('DarkAmber')
welcome_screen()





