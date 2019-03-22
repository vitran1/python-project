def registration():
    import re
    import sqlite3
    conn = sqlite3.connect('OS_Employee.db')

    with conn:
        id = False
        blank_statement = "The field cannot be left blank, please enter a valid input."
        cur = conn.cursor()
        try:
            while not id:
                while True:
                    userID = input("\nPlease enter your Employee ID (Example:1234): ").strip()
                    if userID == '':
                        print(blank_statement)
                    elif userID.isnumeric() == False:
                        print("This field cannot contain letters, decimals, negative numbers, spaces, or special characters.")
                    else:
                        break
                    
                cur.execute("SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '{}')".format(userID))
                results = cur.fetchone()
                if results[0] == 1:
                    print("EmployeeID already exists, please try again.")
                else:
                    id = True
            
            while True:
                userFirst = input("\nPlease enter your First name: ").strip().title()
                if userFirst == '':
                        print(blank_statement)
                elif re.search('^[A-Za-z-]*$', userFirst):
                        break
                else:
                        print("Name must contain only letters.")
                        
            while True:    
                userLast = input("\nPlease enter your Last name: ").strip().title()
                if userLast == '':
                        print(blank_statement)
                elif re.search('^[A-Za-z-]*$', userLast):
                        break
                else:
                        print("Name must contain only letters.")
                    
            while True:
                userEmail = input("\nPlease enter your Gmail address (Example: KobeBeanB@gmail.com): ").strip().lower()
                if userEmail == '':
                        print(blank_statement)
                elif len(userEmail)<11:
                        print("\nPlease enter a valid gmail account.")
                elif userEmail.endswith("@gmail.com") == False:
                        print("\nPlease enter a valid gmail account.")
                else:
                        break
                    
            while True:                       
                userPassword = input("\nPlease enter your password: ").strip().lower()
                x = userPassword
                pw_error = "Password must be at least 4 characters long and contains at least one digit."
                if len(x)<4:
                    print("Error: Insufficient Length - " + pw_error)
                else:
                    break

                        
            cur.execute("INSERT INTO Employee VALUES ('{}','{}','{}','{}','{}')".format(userID, userFirst, userLast, userEmail, userPassword))
            cur.execute("SELECT * FROM Employee WHERE (EmployeeID = '{}')".format(userID))
            results = cur.fetchall()
            print("\nRegistration was successful with the following information - \n \nEmployee ID: " + userID + "\nEmployee Name: " + userFirst + " " + userLast + "\nEmail: " + userEmail + "\nPassword: " + userPassword)
        except:
            print("Connection failed")
    conn.close()
    regend()
    
def regend():
            test = input("1. Return to main menu\n2. Logout and return to login screen\nOPTION: ")
            if test =="":
                print("This field cannot be blank.")
            elif test =="1":
                from menuUI import mainmenu
                mainmenu()
            elif test =="2":
                from Login import login
                login()
            else:
                print("Error Message: Invalid input... please enter a valid number...")
                regend()