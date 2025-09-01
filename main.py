import os
import time

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def Select_User():

    try:
        selection_number = int(input("Select User: "))
    except:
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter A Number Value")
        print("----------------------------------------------")        
        time.sleep(2)
        Start()

    if selection_number == 1:
        selection = 'Admin'
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter Password For " + selection)
        print("----------------------------------------------")
    if selection_number == 2:
        selection = 'Guest'
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter Password For " + selection)
        print("----------------------------------------------")
    if selection_number != 1 and selection_number != 2:
        clear_screen()
        print("----------------------------------------------")
        print("Welcome To The Management Console")
        print("----------------------------------------------")
        print("1 - Admin")
        print("2 - Guest")
        print("----------------------------------------------")
        Select_User()
    
    selection_password = input("Enter Password: ")
    
    if selection == 'Admin' and selection_password == 'Admin':
        clear_screen()
        print("----------------------------------------------")
        print("Welcome Admin, Please Select Desired Action")
        print("----------------------------------------------")
        selection_Actions_Admin()
    if selection == 'Guest' and selection_password == 'Guest':
        clear_screen()
        print("----------------------------------------------")
        print("Welcome Guest, Please Select Desired Action")
        print("----------------------------------------------")
        selection_Actions_Guest()

    if selection == 'Admin' and selection_password != 'Admin':
        clear_screen()
        print("----------------------------------------------")
        print("Welcome To The Management Console")
        print("----------------------------------------------")
        print("1 - Admin")
        print("2 - Guest")
        print("----------------------------------------------")
        Select_User()
    if selection == 'Guest' and selection_password != 'Guest':
        clear_screen()
        print("----------------------------------------------")
        print("Welcome To The Management Console")
        print("----------------------------------------------")
        print("1 - Admin")
        print("2 - Guest")
        print("----------------------------------------------")
        Select_User()

def Start():
    clear_screen()
    print("----------------------------------------------")
    print("Welcome To The Management Console")
    print("----------------------------------------------")
    print("1 - Admin")
    print("2 - Guest")
    print("----------------------------------------------")
    Select_User()

def selection_Actions_Admin():
    clear_screen()
    print("----------------------------------------------")
    print("Welcome To The Admin Management Console")
    print("----------------------------------------------")
    print("0 - Exit")
    print("1 - Marks System")
    print("----------------------------------------------")

    try:
        selection_Admin_Action = int(input("Admin >>> "))
    except:
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter A Number Value")
        print("----------------------------------------------")        
        time.sleep(2)
        selection_Actions_Admin()

    if selection_Admin_Action == 0:
        Start()

    if selection_Admin_Action == 1:
        marks_System()

def selection_Actions_Guest():
    clear_screen()
    print("----------------------------------------------")
    print("Welcome To The Guest Management Console")
    print("----------------------------------------------")
    print("0 - Exit")
    print("----------------------------------------------")

    try:
        selection_Guest_Action = int(input("Guest >>> "))
    except:
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter A Number Value")
        print("----------------------------------------------")        
        time.sleep(2)
        selection_Actions_Guest()

    if selection_Guest_Action == 0:
        Start()

def marks_System():
    try:
        clear_screen()
        print("----------------------------------------------") 
        Mark = int(input("Enter Mark: "))
        clear_screen()
    except:
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter A Number Value")
        print("----------------------------------------------")        
        time.sleep(2)
        marks_System()
    
    if Mark >= 90 and Mark <= 100:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An A+")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 80 and Mark <= 89:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An A")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 70 and Mark <= 79:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An B+")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 60 and Mark <= 69:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An B")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 50 and Mark <= 59:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An C+")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 40 and Mark <= 49:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An C")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 30 and Mark <= 39:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An D+")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 20 and Mark <= 29:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An D")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark >= 0 and Mark <= 19:
        print("----------------------------------------------") 
        print("The Mark " + str(Mark) + "% Translates To An F")
        print("----------------------------------------------") 
        time.sleep(2)
        selection_Actions_Admin()

    if Mark <= -1 or Mark >= 101:
        clear_screen()
        print("----------------------------------------------")
        print("Please Enter A Number Value Between 0 And 100")
        print("----------------------------------------------")        
        time.sleep(2)
        marks_System()

Start()
