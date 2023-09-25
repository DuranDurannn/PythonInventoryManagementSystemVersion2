#Initialize 
def initial():
    try:
        print("First time laucnh setup for PPE Inventory Management System\n")

        #File creation for suppliers.txt
        with open ("suppliers.txt","x") as supplierFile:
            supplierFile.close()

        print("Please insert Supplier Detail\n")

        while True:
            supplierCode = input("Supplier Code: ")
            supplierName = input("Supplier name: ")
            supplierLocation = input("Supplier location: ")

            with open ("suppliers.txt", "at") as supplierFile:
                line = supplierCode + "," + supplierName + "," + supplierLocation + "\n"
                supplierFile.write(line)

            again = (input("Do you want to key in another supplier? Press (Y) to add another, other key to cancel: "))

            print("\n")

            if (again.lower() == "y"):
                pass
            elif (again.lower() != "y"):
                break
        
        supplierFile.close()


        #File creation for hospitals.txt
        with open ("hospitals.txt", "x") as hospitalFile:
            hospitalFile.close()

        print("Please insert Hospital Detail\n")

        while True:
            hospitalCode = input("Hospital Code: ")
            hospitalName = input("Hospital Name: ")
            hospitalLocation = input("Hospital Location: ")

            with open ("hospitals.txt", "at") as hospitalFile:
                line = hospitalCode + "," + hospitalName + "," + hospitalLocation + "\n"
                hospitalFile.write(line)

            again = (input("Do you want to key in another hospital? Press (Y) to add another, other key to cancel: "))

            print("\n")

            if (again.lower() == "y"):
                pass
            elif (again.lower() != "y"):
                break

        hospitalFile.close()

        #File creation for transactions.txt
        open ("transactions.txt", "x")

        #File creation for ppe.txt
        with open ("ppe.txt","x") as ppeFile:
            ppeFile.close()

        while True:
            print("Initial Item Detail\n")

            itemUC = input("Item Code: ")
            itemName = input("Item Name: ")

            with open ("ppe.txt", "at") as ppeFile:
                line = itemUC + "," + itemName + ",100\n"
                ppeFile.write(line)

            again = (input("Do you want to key in another item? Press (Y) to add another, other key to cancel: "))

            if (again.lower() == "y"):
                pass
            elif (again.lower() != "y"):
                break

        ppeFile.close()

        #File creation for usres.txt and also an admin account
        with open("users.txt", "x") as userFile:
            allUsers = "admin,123,A"
            strAllUsers = str(allUsers)
            userFile.write(strAllUsers)
            userFile.close()
        
        print("Initialization completed... All files have been created\n")
        print("Default username and password for admin is: admin 123\n")
    except:
        pass

#Login
def login(usrname, passwrd, admin):
    with open("users.txt", "r") as loginFile:
        db = [[str(n) for n in line.strip().split(",")] for line in loginFile.readlines() if line.strip()]

    loginStat = False

    #Checking user
    for x in range(0, len(db)):
        if (usrname == db[x][0] and passwrd == db[x][1]):
            loginStat = True
            if (db[x][2] == "A"):
                adminMainMenu()
                admin = True
                return admin
            elif (db[x][2] == "S"):
                mainMenu()
                admin = False
                return admin
    
    if loginStat:
        pass
    else:
        print("Incorrect password or username. Please try again or contact admin for assistant!")

#Admin main menu
def adminMainMenu():
    while True:
        print("=========================")
        print("\nWelcome to PPE Inventory Management System\n")
        print("1. Inventory")
        print("2. Supplier")
        print("3. Hospital")
        print("4. Transaction")
        print("5. Users")
        print("6. Logout")
        print("=========================")

        option = input("Please selct an option: ")
        admin = True

        if (option == "1"):
            inventory(admin)
        elif (option == "5"):
            users()
        else:
            print("\nThere is no such option")

def mainMenu():
    while True:
        print("\nWelcome to PPE Inventory Management System\n")
        print("1. Inventory")
        print("2. Supplier")
        print("3. Hospital")
        print("4. Transaction")
        print("5. Logout")
        print("=========================")
            
        option = input("Please selct an option: ")
        admin = False

        if (option == "1"):
            inventory(admin)
        else:
            print("\nThere is no such option")

def inventory(admin):         
    while True:
        with open("ppe.txt", "r") as ppeFile:
            ppeDB = [[str(n) for n in line.strip().split(",")] for line in ppeFile.readlines() if line.strip()]

        print("\nPPE Inventory Management\n")

        print("1. View Inventory")
        print("2. Add Inventory")
        print("3. Distribute Inventory")
        print("4. Back")

        print("===============")
        option = input("Select an option: ")
        print("===============")

        #Viewving Inventory-----------------------------------------------------------------------
        if (option == "1"):
            print("\nViewing inventory...\n")

            print("___________________________________________")
            print("|{:^15}|{:^15}|{:^10}|".format("Item Code", "Item Name", "Quantity"))
            print("|------------------------------------------|")
            for x in range(len(ppeDB)):
                print("|{:^15}|{:^15}|{:^10}|".format(ppeDB[x][0], ppeDB[x][1], ppeDB[x][2]))
            print("|__________________________________________|")
        
        #Adding Inventory-----------------------------------------------------------------------
        elif (option == "2"):
            print("\nAdding inventory...\n")

            itemCode = input("Item code: ")

            #Search for item item code
            for x in range(0, len(ppeDB)):
                if (itemCode == ppeDB[x][0]):
                    search = ppeDB[x][0]
                    key = x
                    break
                else:
                    search = ppeDB[x][0]
                    pass        

            if (search == itemCode):
                #Show the item quantity before and after adding (also all the calculation)
                print("Current quantity: " + ppeDB[key][2])

                itemQuantity = input("\nAmount adding to inventory: ")

                total = int(ppeDB[key][2]) + int(itemQuantity)
                print("\nQuantity after adding: " + str(total))

                confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                if (confirm.lower() == "y"):
                    ppeDB[key][2] = total

                    #Write into ppe.txt
                    with open("ppe.txt", "wt") as ppeFile:
                        for x in range(len(ppeDB)):
                            line = "{},{},{}\n".format(ppeDB[x][0], ppeDB[x][1], ppeDB[x][2])
                            ppeFile.write(line)
                    
                    print("\nOperation successful")
                    print("____________________")
                else:
                    print("\nOperation canceled")
                    print("____________________")
            else:
                print("\nInvalid item code")
                print("____________________")
            
            ppeFile.close()

        #Distributing Inventory-----------------------------------------------------------------------
        elif (option == "3"):
            print("Distributing Inventory...\n")

            itemCode = input("Item code: ")

            #Search for item code
            for x in range(0, len(ppeDB)):
                if (itemCode == ppeDB[x][0]):
                    search = ppeDB[x][0]
                    key = x
                    break
                else:
                    search = ppeDB[x][0]
                    pass
            
            if (search == itemCode):
                #Show the item quantity before and after distributing
                print("Current quantity: " + ppeDB[key][2])

                itemQuantity = input("\nAmount distibuting: ")

                if (int(ppeDB[key][2]) >= int(itemQuantity)):
                    total = int(ppeDB[key][2]) - int(itemQuantity)
                    print("\nQuantity after distributing: " + str(total))

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")
                else:
                    print("\nNot enough stock")

                if (confirm.lower() == "y"):
                    ppeDB[key][2] = total

                    #Write into ppe.txt
                    with open("ppe.txt", "wt") as ppeFile:
                        for x in range(len(ppeDB)):
                            line = "{},{},{}\n".format(ppeDB[x][0], ppeDB[x][1], ppeDB[x][2])
                            ppeFile.write(line)
                    
                    print("\nOperation successful")
                    print("____________________")
                else:
                    print("\nOperation canceled")
                    print("____________________")
            else:
                print("\nInvalid item code")
                print("____________________")


            ppeFile.close()

        #Back-----------------------------------------------------------------------
        elif (option == "4"):
            if admin:
                adminMainMenu()
            else:
                mainMenu()
        else:
            print("Invalid option, please try again")
            print("____________________")

def users():
    while True:
        with open("users.txt", "r") as usersFile:
            usersDB = [[str(n) for n in line.strip().split(",")] for line in usersFile.readlines() if line.strip()]

        print("\nPPE Admin Users Management\n")

        print("1. View All Users")
        print("2. Add Users")
        print("3. Edit Users")
        print("4. Delete Users")
        print("5. Back")

        print("===============")
        option = input("Select an option: ")
        print("===============")

        #Viewving Users-----------------------------------------------------------------------
        if (option == "1"):
            print("\nViewing all users...\n")

            print("________________________________________________")
            print("|{:^15}|{:^15}|{:^15}|".format("username", "Password", "Authority"))
            print("|-----------------------------------------------|")
            for x in range(len(usersDB)):
                print("|{:^15}|{:^15}|{:^15}|".format(usersDB[x][0], usersDB[x][1], usersDB[x][2]))
            print("|_______________________________________________|")

        #Adding Users-----------------------------------------------------------------------
        elif (option == "2"):
            print("\nAdding users...\n")

            newUser = input("New username: ")

            #Search for the same username
            for x in range(0, len(usersDB)):
                if (newUser == usersDB[x][0]):
                    dupe = True
                    print("\nUsername " + usersDB[x][0] + " has been taken, please try again")
                else:
                    dupe = False
            
            if (dupe == True):
                break
            #If false, admin will be able to set the password and authority
            else:
                newPassword = input("New password: ")
                authority = input("Authorization (A / S): ")

                confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                if (confirm.lower() == "y"):
                    if (authority.lower() == "a" or "s"):
                        #Append into users.txt
                        with open("users.txt", "at") as usersFile:
                            line = "{},{},{}\n".format(newUser, newPassword, authority.upper())
                            usersFile.write(line)

                        print("\nOperation successful")
                        print("____________________")
                    else:
                        print("\nInvalid authority status!")
                        print("____________________")
                else:
                    print("\nOperation canceled")
                    print("____________________")
        
        #Editing Users-----------------------------------------------------------------------
        elif (option == "3"):
            print("Editing users...\n")

            editUser = input("User to edit: ")

            #Search for user
            for x in range(0, len(usersDB)):
                if (editUser == usersDB[x][0]):
                    search = usersDB[x][0]
                    key = x
                    break
                else:
                    search = usersDB[x][0]
                    pass

            if (search == editUser):
                print("\nCurrent username: " + usersDB[key][0])
                print("Current password: " + usersDB[key][1])
                print("Current authorization: " + usersDB[key][2])

                newUsername = input("\nNew username: ")
                newPassword = input("New password: ")
                newAuthority = input("New authorization: ")

                confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                if (confirm.lower() == "y"):
                    usersDB[key][0] = newUsername
                    usersDB[key][1] = newPassword
                    usersDB[key][2] = newAuthority

                    #Write into users.txt
                    with open("users.txt", "wt") as usersFile:
                        for x in range(0, len(usersDB)):
                            line = "{},{},{}\n".format(usersDB[x][0], usersDB[x][1], usersDB[x][2].upper())
                            usersFile.write(line)
                    
                    print("\nOperation successful")
                    print("____________________")
                else:
                    print("\nOperation canceled")
                    print("____________________")
            else:
                print("\nUsername cant be found in database")
                print("____________________")

        #Deleting Users-----------------------------------------------------------------------
        elif (option == "4"):
            print("Deleting users...\n")
        
            deleteUser = input("Username: ")

            #Search for user
            for x in range(0, len(usersDB)):
                if (deleteUser == usersDB[x][0]):
                    search = usersDB[x][0]
                    key = x
                    break
                else:
                    search = usersDB[x][0]
                    key = x
                    pass

            print("Are you really sure you want to delete " + search + " from database")

            confirm = input("\nPress (Y) to confirm, other key to cancel: ")

            #If true, pop the inputted user
            if (confirm.lower() == "y"):
                del usersDB[key]
            
                #Write into users.txt
                with open("users.txt", "wt") as usersFile:
                    for x in range(len(usersDB)):
                        line = "{},{},{}\n".format(usersDB[x][0], usersDB[x][1], usersDB[x][2])
                        usersFile.write(line)

                print("\nOperation successful")
                print("____________________")
            else:
                print("\nOperation canceled")
                print("____________________")

        #Back-----------------------------------------------------------------------
        elif (option == "5"):
            adminMainMenu()
        else:
            print("Invalid option, please try again")
            print("____________________")

    usersFile.close()

#Main Logic
while True:
    stat = False
    initial()

    print("PPE Inventory Mangement System\n")

    username = str(input("Username: "))
    password = str(input("Password: "))

    log = login(username, password, stat)

    print("\n")

    if log:
        admin = True
    else:
        admin = False