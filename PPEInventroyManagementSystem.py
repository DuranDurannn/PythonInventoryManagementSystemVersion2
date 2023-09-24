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
    with open("users.txt" ,"r") as f:
        db = [[str(n) for n in line.strip().split(",")] for line in f.readlines() if line.strip()]

    #Checking user
    loginStat = False

    for x in range(0, len(db)):
        if (usrname == db[x][0] and passwrd == db[x][1]):
            loginStat = True
            if (db[x][2] == "A"):
                adminMainMenu()
                admin = True
                return admin
            if (db[x][2] == "S"):
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

        try:
            option = int(input("Please selct an option: "))
            admin = True
        except:
            print("\nOnly numbers can be input, please try again")

def mainMenu():
    while True:
        print("\nWelcome to PPE Inventory Management System\n")
        print("1. Inventory")
        print("2. Supplier")
        print("3. Hospital")
        print("4. Transaction")
        print("5. Logout")
        print("=========================")
            
        try:
            option = int(input("Please selct an option: "))
            admin = False
        except:
            print("\nOnly numbers can be input, please try again")

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