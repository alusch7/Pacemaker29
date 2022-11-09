# -*- coding: utf-8 -*-

#Group 29 - DCM GUI for Pacemaker - 3K04

import PySimpleGUI as sg
import sys
import os
from DCM_Functions import *


import serial

s = serial.Serial('COM4',115200,timeout = 10)
#s = ser.read(100)
print("Opening: " + s.name)

for i in range(10):
    s.write(123)


s.close()

pacemaker_connected = False

#pacemaker_connected = True


# Welcome Screen function
def welcome_screen():
    #print("CCCC")
    # Create Text and buttons

    #Checking the connection status of the Pacemaker to the program
    #if(pacemaker_connected):
    #    connection_string = "Connected"
    #    connection_colour = "Green"
    #else:
    #   connection_string = "Disconnected"
    #    connection_colour = "red"

    #Acquires the information to tbe displayed based on the connectivity status of the Pacemaker
    connection_string = get_connection_string(pacemaker_connected)
    connection_colour = get_connection_color(pacemaker_connected)
    
    layout1 = [
        #Creating modules for the welcome screen
                [sg.Text("Pacemaker: " + connection_string, justification='r',text_color=connection_colour)], 
                [sg.Text("Welcome Page", justification='center')], 
                [sg.Button("Register New User",size=(10,2))], 
                [sg.Button("Login As Existing User",size=(10,2))]
                
              ]

    # Create the window
    window1 = sg.Window("Welcome", layout1,size=(1600, 800) ,resizable=True)
    #sg.Popup('SUCCESFULLY REGISTERED', keep_on_top=True)
    # Create an event loop
    while True:
        
        # Read the event name and any inputs given
        event, values = window1.read()
        
        # Sets flag to go to different pages depending on button click
        flag = 0
        if (event == "Register New User"):
            flag = 1
            
            break
        elif(event == "Login As Existing User"):
            flag = 2
            break
        elif (event == sg.WIN_CLOSED):
            break
    
    # CLose the window and go to pressed page
    window1.close()
    
    if(flag == 1):
        registry()
       # print("BBBBB")
    elif(flag == 2):
        login()
        
def registry():
   
    # Ask User to enter new user information   
    if(pacemaker_connected):
        connection_string = "Connected"
        connection_colour = "Green"
    else:
        connection_string = "Disconnected"
        connection_colour = "red"
    
    layout1 = [
    #Creating modules for the Registering of the Parameters
                
    [sg.Text("Pacemaker: " + connection_string, justification='r',text_color=connection_colour)], 
     [sg.Text("Register New User", justification='center')],    
    [sg.Text('Please enter a new username and password')],
    [sg.Text('username', size =(15, 1)), sg.InputText()],
    [sg.Text('password', size =(15, 1)), sg.InputText(key='Password', password_char='*')],
    
    [sg.Text("Set Patient Variables", justification='center')],    
   [sg.Text('Please enter the user\'s heart information')],
    [sg.Text('Lower Rate Limit', size =(15, 1)), sg.InputText()],
    [sg.Text('Upper Rate Limit', size =(15, 1)), sg.InputText()],
    [sg.Text('Atrial Amplitude', size =(15, 1)), sg.InputText()],
    [sg.Text('Atrial Pulse Width', size =(15, 1)), sg.InputText()],
    #[sg.Text('')],
    [sg.Text('Ventricular', size =(15, 1)), sg.InputText()],
    [sg.Text('Amplitude')],
    [sg.Text('Ventricular', size =(15, 1)), sg.InputText()],
    [sg.Text('Pulse Width')],
    [sg.Text('VRP', size =(15, 1)), sg.InputText()],
    [sg.Text('ARP', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Button("Go Back",size=(7,1))]
    ]
    
    # Open user information
    login_info = open("Login_Info.txt","a+") 
    heart_info = open("Heart_Info.txt","a+") 
    num_users_file = open("NUM_USERS.txt","r")
    #print("Number of users: ")
    num_users = int(num_users_file.readline())
    #print(num_users)
    num_users_file.close()
    
    
    # Create the window
    window1 = sg.Window("Registry", layout1,size=(1600, 800) ,resizable=True)
    username_exists = False
    # Create an event loop
    while True:
        # Read the event name and any inputs given
        event, values = window1.read()
        
        
        flag = 0
        # Check if 10 users have been added
        if (event == "Go Back"):
            flag = 1
            #print("AAAAAA")
            break
        isLetter = False
        
        if (num_users < 10): #Limiting the number of users to 10
            if (event == "Submit"):
               
                # If not append the list of users and increment number of users by 1
                
                with open("Login_Info.txt", "r") as filestream:  
                    
                    for line in filestream:
                        
                        currentline = line.split(",")
                      
                        # Check the given username and password against all in the file
                       
                        
                       
                        
                        if (currentline[0] == values[0]):
            
                            username_exists = True
                            
                    for i in range (0,8):
                        if(not(values[i].isnumeric())):
                            isLetter = True

                    if(len(values[0]) >= 3):
                        if(len(values[1]) >= 3):
                            if(values [0] > 50): #LRL > 50
                                if (values [1] < 130): # URL < 130
                                    if (values[0] > values [1]):
                                        
    
                            
                                        if (not(isLetter)): #Checks if the value is indeed a number and not some random value
                                            if(not(username_exists)): # Checking if the username exists -> Writes the value if false
                                                login_info.write(values[0] + "," + values[1] + "\n")
                                                heart_info.write(values[2] + "," + values[3] + "," + values[4] + "," + values[5] + "," + values[6] + "," + values[7] + "," + values[8] + "," + values[9] + "\n")
                                                num_users_file = open("NUM_USERS.txt","w")
                                                num_users_file.write(str(num_users+1))
                          
                                                sg.Popup('SUCCESFULLY REGISTERED', keep_on_top=True)
                                                flag = 1
                                                break
                                            else:
                                                sg.Popup('Username already exists. Try a new one.', keep_on_top=True)
                                                flag = 2
                                                break
                                            
                                        else:
                                            sg.Popup('A non numeric character was entered, please try again!', keep_on_top=True)
                                            flag = 2
                                            #break
                                    else:
                                        sg.Popup('Lower rate limit cannot be higher than the upper rate limit, please try again!', keep_on_top=True)
                                        flag = 2
                                        #break        
                                else:
                                    sg.Popup('Upper rate limit is too high, please try again!', keep_on_top=True)
                                    flag = 2
                                    #break    
                                    
                            else:
                                sg.Popup('Lower rate limit is too low, please try again!', keep_on_top=True)
                                flag = 2
                        else:
                            sg.Popup('Password is too short, please try again!', keep_on_top=True)
                            flag = 2           
                    else:
                        sg.Popup('Username is too short, please try again!', keep_on_top=True)
                        flag = 2
                
                break                
            elif (event == sg.WIN_CLOSED): #When the window is closed will break out and finish the window
               
                break
        else:
            # Pop up that there are too many users
            sg.Popup('TOO MANY USERS REGISTERED', keep_on_top=True)
            flag = 1
            break
    window1.close()
    login_info.close()
    heart_info.close()
    num_users_file.close()

    if(flag == 1): #Flag determines the next window to open
        welcome_screen()
    elif (flag == 2):
        registry()
        
    
    
def login(): #Creating the welcome screen for the login page
    
    if(pacemaker_connected):
        connection_string = "Connected"
        connection_colour = "Green"
    else:
        connection_string = "Disconnected"
        connection_colour = "red"
    
    layout1 = [
    [sg.Text("Pacemaker: " + connection_string, justification='r',text_color=connection_colour)], 
     [sg.Text("Login", justification='center')],    
    [sg.Text('Please enter your username and password')],
    [sg.Text('username', size =(15, 1)), sg.InputText()],
    [sg.Text('password', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Button("Go Back",size=(7,1))]
    ]
    
    login_info = open("Login_Info.txt","r+") 
    num_users_file = open("NUM_USERS.txt","r")
    #print("Number of users: ")
    num_users = int(num_users_file.readline())
    #print(num_users)

    # Create the window
    window1 = sg.Window("Login", layout1,size=(1600, 800) ,resizable=True)

    
    # Create an event loop
    while True:
        event, values = window1.read()
       
        flag = 0
        
        if (event == "Go Back"): #Checks if the back button has been pressed
            flag = 2
            break
        
        if (event == "Submit"): #Checks if the submit button has been pressed
    
            access = False
            with open("Login_Info.txt", "r") as filestream:
                user_num = 0
                for line in filestream:
                    #print("AAAAAAA: " + str(user_num))
                    currentline = line.split(",")
                   # currentline = line.split("\n")
                    # Check the given username and password against all in the file
#                    print(currentline[0])
                   # print(currentline[1])
                  #  print(values[0])
                  #  print(values[1])
                    if (currentline[0] == values[0] and currentline[1] == values[1] + "\n"):
                        access = True
                        break
                    user_num += 1

                            
            if (access): #Is the password and the username the same?
                sg.Popup('ACCESS GRANTED', keep_on_top=True)
                
                #print("ACCESS GRANTED")
                flag = 1
                break
            else:
                sg.Popup('ACCESS DENIED', keep_on_top=True)
                #print("ACCESS DENIED")
            
        
        
        elif (event == sg.WIN_CLOSED):
           
            break
    
        
    login_info.close()
    num_users_file.close()    
        
    window1.close() 

    if (flag == 1):
        logged_in_screen(user_num,values[0],num_users)
    elif (flag == 2):
        welcome_screen()


def logged_in_screen (user_num,username,num_users):

    #Creates the "logged in screen" page after the user has successfully logged in.
    
    
    if(pacemaker_connected):
        connection_string = "Connected"
        connection_colour = "Green"
    else:
        connection_string = "Disconnected"
        connection_colour = "red"
    
    layout1 = [
        
                
                [sg.Text("Pacemaker: " + connection_string, justification='r',text_color=connection_colour)], 
                [sg.Text(username, justification='center')], 
                [sg.Button("AOO",size=(10,2))], 
                [sg.Button("VOO",size=(10,2))],
                [sg.Button("VVI",size=(10,2))], 
                [sg.Button("AAI",size=(10,2))],
                [sg.Button("View/Edit Parameters",size=(10,2))],
                [sg.Button("Go Back (Logout)",size=(10,2))]
              ]

     # Create the window
    window1 = sg.Window("User Menu", layout1,size=(1600, 800) ,resizable=True)
    
     # Create an event loop
    while True:
    
        # Read the event name and any inputs given
        event, values = window1.read()
        
        # Sets flag to go to different pages depending on button click
        flag = 0
        if (event == "VOO"):
            flag = 1  
            break
        elif(event == "AOO"):
            flag = 2
            break
        elif(event == "VVI"):
            flag = 3
            break
        elif(event == "AAI"):
            flag = 4
            break
        elif(event == "View/Edit Parameters"):
            flag = 5
            break
        elif(event == "Go Back (Logout)"):
            flag = 6
            break
        elif (event == sg.WIN_CLOSED):
            break
    
    # CLose the window and go to pressed page
    window1.close()
    
    #Begins checking the button pressed, each statement will open a different function and send the necessary parameters

    if(flag == 1): 
        VOO(user_num,username,num_users)
    elif(flag == 2):
        AOO(user_num,username,num_users)
    elif(flag == 3):
        VVI(user_num,username,num_users)
    elif(flag == 4):
        AAI(user_num,username,num_users)
    elif (flag == 5):
        display_and_edit_Info(user_num,username,num_users)
    elif(flag == 6):
        login()
        

def AOO(user_num,username,num_users): #AOO Opearting Mode Window
    layout1 = [
    
    [sg.Button("Go Back",size=(10,2))]
      ]
    
    # Create the window
    window1 = sg.Window("AOO", layout1,size=(1600, 800) ,resizable=True)
       
# Create an event loop
    while True:
   
       # Read the event name and any inputs given
       event, values = window1.read()
       
       # Sets flag to go to different pages depending on button click
       flag = 0
       if (event == "Go Back"):
           flag = 1  
           break

   
   # CLose the window and go to pressed page
    window1.close()
   
    if(flag == 1):
        logged_in_screen (user_num,username,num_users)
        pass
    
    
def VOO(user_num,username,num_users): #VOO Operating Mode Window
   layout1 = [
    
    [sg.Button("Go Back",size=(10,2))]
      ]
    
    # Create the window
   window1 = sg.Window("VOO", layout1,size=(1600, 800) ,resizable=True)
       
     # Create an event loop
   while True:
   
       # Read the event name and any inputs given
       event, values = window1.read()
       
       # Sets flag to go to different pages depending on button click
       flag = 0
       if (event == "Go Back"):
           flag = 1  
           break

   
   # CLose the window and go to pressed page
   window1.close()
   
   if(flag == 1):
        logged_in_screen (user_num,username,num_users)
        pass
def VVI(user_num,username,num_users): #VVI Operating Mode Window
    layout1 = [
    
    [sg.Button("Go Back",size=(10,2))]
      ]
    
    # Create the window
    window1 = sg.Window("VVI", layout1,size=(1600, 800) ,resizable=True)
       
    # Create an event loop
    while True:
   
       # Read the event name and any inputs given
       event, values = window1.read()
       
       # Sets flag to go to different pages depending on button click
       flag = 0
       if (event == "Go Back"):
           flag = 1  
           break

   
   # CLose the window and go to pressed page
    window1.close()
   
    if(flag == 1):
        logged_in_screen (user_num,username,num_users)
        pass
    
def AAI(user_num,username,num_users): #AAI Operating Mode Window
    layout1 = [
    
    [sg.Button("Go Back",size=(10,2))]
      ]
    
    # Create the window
    window1 = sg.Window("AAI", layout1,size=(1600, 800) ,resizable=True)
       
    # Create an event loop
    while True:
   
       # Read the event name and any inputs given
       event, values = window1.read()
       
       # Sets flag to go to different pages depending on button click
       flag = 0
       if (event == "Go Back"):
           flag = 1  
           break

   
   # CLose the window and go to pressed page
    window1.close()
   
    if(flag == 1):
        logged_in_screen (user_num,username,num_users)
        pass

def display_and_edit_Info(user_num,username,num_users): 
    #Creates the window where one can change and edit all the necessary parameters for the patient
    
    
    with open("Heart_Info.txt", "r") as filestream:
        
        #login_info = open("Login_Info.txt","r+") 
        count = 0
        for line in filestream:
           # print("BBBBB: " + str(user_num))
            currentline = line.split(",")
            
            if (count == user_num):
                if(pacemaker_connected):
                    connection_string = "Connected"
                    connection_colour = "Green"
                else:
                    connection_string = "Disconnected"
                    connection_colour = "red"
                
                layout1 = [
                    
                            
                [sg.Text("Pacemaker: " + connection_string, justification='r',text_color=connection_colour)], 
                [sg.Text("Set Patient Variables", justification='center')],    
                [sg.Text('Enter new data to replace existing values')],
                [sg.Text('Lower Rate Limit: ' + currentline[0], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Upper Rate Limit: ' + currentline[1], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Atrial Amplitude: ' + currentline[2], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Atrial Pulse Width: ' + currentline[3], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Ventricular Amplitude: ' + currentline[4], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Ventricular Pulse Width: ' + currentline[5], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],     
                [sg.Text('VRP: ' + currentline[6], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('ARP: ' + currentline[7], size =(25, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Button("PRESS TO CONFIRM EDITS",size=(10,3))],
                [sg.Button("Go Back",size=(10,3))]
                ]
            count+=1


    # Create the window
    window1 = sg.Window("View Data", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    flag = 0
    
    while True:
        isLetter = False
        event, values = window1.read()
       
        if (event == "Go Back"):  
            flag = 2
            break
       
       
        if (event == "PRESS TO CONFIRM EDITS"):    
            flag = 1
            with open("Heart_Info.txt", "r") as filestream:
                
                write_info = [ [] for i in range(num_users)]
                
                #login_info = open("Login_Info.txt","r+") 
                count = 0
                for line in filestream:

                    currentline = line.split(",")
                    
                    if (count != user_num):
                    
                        for i in range (8):
                            write_info[count].append(currentline[i])
                    else:
                        for i in range (8):
                            if (values[i] == ""):
                                write_info[count].append(currentline[i])
                            else:
                               # write_info[count].append(values[i])
                                if (values[i].isnumeric()):
                                    if(i != 7):
                                        write_info[count].append(values[i])
                                    else:
                                        write_info[count].append(values[i] + "\n")
                                else:
                                    isLetter = True
                                    break
                    
                    count+=1
            #print(write_info)

            if(values [0] > 50): #LRL > 50
                if (values [1] < 130): # URL < 130
                    if (values[0] > values [1]):
                        

            
                        if (not(isLetter)): #Checks if the value is indeed a number and not some random value
            
                            with open("Heart_Info.txt", "w") as filestream:
                                
                              #  write_info = [ [] for i in range(num_users)]
                                
                                #login_info = open("Login_Info.txt","r+") 
                                count = 0
                                for i in range(num_users):

                                    
                                        with open("Heart_Info.txt", "w") as filestream:
                                            
                                          #  write_info = [ [] for i in range(num_users)]
                                            
                                            #login_info = open("Login_Info.txt","r+") 
                                            count = 0
                                            for i in range(num_users):
                                                
                                                for j in range(8):
                                                    filestream.write(write_info[i][j])
                                                    
                                                    if (j != 7):
                                                        filestream.write(",")
                            
                                            break
                                        
                                        pass
                        else:
                            sg.Popup('A non numeric character was entered, please try again!', keep_on_top=True)
                            flag = 1
                            #break
                    else:
                        sg.Popup('Lower rate limit cannot be higher than the upper rate limit, please try again!', keep_on_top=True)
                        flag = 1
                        #break        
                else:
                    sg.Popup('Upper rate limit is too high, please try again!', keep_on_top=True)
                    flag = 1
                    #break    
                    
            else:
                sg.Popup('Lower rate limit is too low, please try again!', keep_on_top=True)
                flag = 1
                
            
        elif (event == sg.WIN_CLOSED):
           
            break
        
    window1.close()  
    
    if(flag == 1):
        display_and_edit_Info(user_num,username,num_users)
    elif (flag == 2):
        logged_in_screen(user_num,username,num_users)

sg.theme('DarkAmber')

#The program begins with the Welcome Screen Page
welcome_screen()





