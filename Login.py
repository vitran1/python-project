def login():

    import sqlite3
    conn = sqlite3.connect('OS_Employee.db')

    with conn:
        loginTest = False
        while not loginTest:
            cur = conn.cursor()
            try:
                while True:
                    userEmail = input("\nPlease enter your email address (example: donald.sutherland@gmail.com): ").strip().lower()
                    if userEmail != "" and '@' in userEmail:
                        cur.execute("SELECT COUNT (*) FROM Employee WHERE (Email = '{}')".format(userEmail))
                        results = cur.fetchone()
                        if results[0] == 1:
                            break
                        else:
                            print("The user email does not exist, please try again.")
                    else:
                        print("The field cannot be left blank or The user email must follow the format of the example given.")
                
                while True:   
                    userPassword = input("\nPlease enter your email password: ").strip().lower()
                    if userPassword != "":
                        cur.execute("SELECT COUNT (*) FROM Employee WHERE (Password = '{}')".format(userPassword))
                        results = cur.fetchone()
                        if results[0] == 1:
                            break
                        else:
                            print("The user password is incorrect, please try again.")
                    else:
                        print("The field cannot be left blank.")
                
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + userEmail + "' AND Password = '" + userPassword + "')")
                results = cur.fetchone()
                #print(results[0])
                if results[0] == 1:
                    print("==================login successful!==================\n")
                    loginTest= True
                    from menuUI import mainmenu
                    mainmenu()
                else:
                    print("Login unsuccessful. Please try logging in again.")
            except:
                print("Connection Failed")
    
    conn.close()


