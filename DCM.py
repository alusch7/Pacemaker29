# -*- coding: utf-8 -*-

import PySimpleGUI as sg

# Welcome Screen function
def welcome_screen():
    
    # Create Text and buttons
    layout1 = [
                [sg.Text("Welcome Page", justification='center')], 
                [sg.Button("Register New User",size=(10,2))], 
                [sg.Button("Login As Existing User",size=(10,2))]
                
              ]

    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

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
    elif(flag == 2):
        login()
        
def registry():
   
    # Ask User to enter new user information   
    layout1 = [
     [sg.Text("Register New User", justification='center')],    
    [sg.Text('Please enter a new username and password')],
    [sg.Text('username', size =(15, 1)), sg.InputText()],
    [sg.Text('password', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
    ]
    
    # Open user information
    login_info = open("Login_Info.txt","a+") 
    num_users_file = open("NUM_USERS.txt","r")
    print("Number of users: ")
    num_users = int(num_users_file.readline())
    print(num_users)
    num_users_file.close()
    
    
    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    while True:
        # Read the event name and any inputs given
        event, values = window1.read()
      
        
        flag = 0
        # Check if 10 users have been added
        if (num_users < 10):
            if (event == "Submit"):
               
                # If not append the list of users and increment number of users by 1
                login_info.write(values[0] + "," + values[1] + "\n")
                num_users_file = open("NUM_USERS.txt","w")
                num_users_file.write(str(num_users+1))
                sg.Popup('SUCCESFULLY REGISTERED', keep_on_top=True)
                flag = 1
                break
            elif (event == sg.WIN_CLOSED):
               
                break
        else:
            # Pop up that there are too many users
            sg.Popup('TOO MANY USERS REGISTERED', keep_on_top=True)
            flag = 1
            break
    window1.close()
    login_info.close()
    num_users_file.close()
    if(flag == 1):
        welcome_screen()
    
    
def login():
    layout1 = [
     [sg.Text("Login", justification='center')],    
    [sg.Text('Please enter your username and password')],
    [sg.Text('username', size =(15, 1)), sg.InputText()],
    [sg.Text('password', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
    ]
    
    login_info = open("Login_Info.txt","r+") 
    num_users_file = open("NUM_USERS.txt","r")
    print("Number of users: ")
    num_users = int(num_users_file.readline())
    print(num_users)

    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    while True:
        event, values = window1.read()
       
        flag = 0
        if (event == "Submit"):
    
            access = False
            with open("Login_Info.txt", "r") as filestream:
                for line in filestream:

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

                            
            if (access):
                sg.Popup('ACCESS GRANTED', keep_on_top=True)
                print("ACCESS GRANTED")
                
            else:
                sg.Popup('ACCESS DENIED', keep_on_top=True)
                print("ACCESS DENIED")
            
            
           
        elif (event == sg.WIN_CLOSED):
           
            break
        
    login_info.close()
    num_users_file.close()    
        
    window1.close()     


    
sg.theme('DarkAmber')
welcome_screen()





