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
                flag = 1
                break
            else:
                sg.Popup('ACCESS DENIED', keep_on_top=True)
                print("ACCESS DENIED")
            
        
        
        elif (event == sg.WIN_CLOSED):
           
            break
    
        
    login_info.close()
    num_users_file.close()    
        
    window1.close() 

    if (flag == 1):
        logged_in_screen(0,values[0],num_users)    


def logged_in_screen (user_num,username,num_users):
    
  
    
    
    layout1 = [
                [sg.Text(username, justification='center')], 
                [sg.Button("AOO",size=(10,2))], 
                [sg.Button("VOO",size=(10,2))],
                [sg.Button("VVI",size=(10,2))], 
                [sg.Button("AAI",size=(10,2))],
                [sg.Button("View/Edit Parameters",size=(10,2))],
                
              ]

     # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)
    
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
        elif (event == sg.WIN_CLOSED):
            break
    
    # CLose the window and go to pressed page
    window1.close()
    
    if(flag == 1):
        VOO()
    elif(flag == 2):
        AOO()
    elif(flag == 3):
        VVI()
    elif(flag == 4):
        AAI()
    elif (flag == 5):
        display_and_edit_Info(user_num,num_users)
        

def AOO(user_num):
    pass
def VOO(user_num):
    pass
def VVI(user_num):
    pass
def AAI(user_num):
    pass
    

def display_and_edit_Info(user_num,num_users):
    
    
    
    with open("Heart_Info.txt", "r") as filestream:
        
        #login_info = open("Login_Info.txt","r+") 
        count = 0
        for line in filestream:

            currentline = line.split(",")
            
            if (count == user_num):
                layout1 = [
                [sg.Text("Set Patient Variables", justification='center')],    
                [sg.Text('Enter new data to replace existing values')],
                [sg.Text('Lower Rate Limit: ' + currentline[0], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Upper Rate Limit: ' + currentline[1], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Atrial Amplitude: ' + currentline[2], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Atrial Pulse Width: ' + currentline[3], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Ventricular Amplitude: ' + currentline[4], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('Ventricular Pulse Width: ' + currentline[5], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],     
                [sg.Text('VRP: ' + currentline[6], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Text('ARP: ' + currentline[7], size =(20, 1))],
                [sg.Text( size =(15, 1)), sg.InputText()],
                [sg.Button("PRESS TO CONFIRM EDITS",size=(10,3))],
                ]
            count+=1


    # Create the window
    window1 = sg.Window("Demo", layout1,size=(1600, 800) ,resizable=True)

    # Create an event loop
    flag = 0
    while True:
        event, values = window1.read()
       
        
       
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
                                write_info[count].append(values[i])
                    
                    count+=1
            print(write_info)
            with open("Heart_Info.txt", "w") as filestream:
                
              #  write_info = [ [] for i in range(num_users)]
                
                #login_info = open("Login_Info.txt","r+") 
                count = 0
                for i in range(num_users):
                    
                    for j in range(8):
                        filestream.write(write_info[i][j])
                        
                        if(j == 7):
                            pass
                            #filestream.write("\n")
                        else:
                            filestream.write(",")

                break
            
            pass
        elif (event == sg.WIN_CLOSED):
           
            break
        
    window1.close()  
    
    if(flag == 1):
        display_and_edit_Info(user_num,num_users)
    
sg.theme('DarkAmber')
welcome_screen()





