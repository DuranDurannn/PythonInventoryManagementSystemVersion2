import datetime

#Initialize 
def initial():
    try:
        #File creation for transactions.txt
        with open ("transactions.txt", "x") as transactionFile:
            transactionFile.close()

        #File creation for suppliers.txt
        with open ("suppliers.txt","x") as supplierFile:
            supplierFile.close()

        print("Please insert Supplier Detail (At least 2 and at most 4 supplier can be store in database)\n")

        for x in range(0, 4):
            supplierCode = input("Supplier Code: ")
            supplierName = input("Supplier name: ")
            supplierLocation = input("Supplier location: ")
            suppliedItemCode = input("Supplying item code (Insert / in between item code): ")

            with open ("suppliers.txt", "at") as supplierFile:
                line = supplierCode + "," + supplierName + "," + supplierLocation + "," + suppliedItemCode + "\n"
                supplierFile.write(line)
                supplierFile.close()

            again = (input("\nDo you want to key in another supplier? Press (Y) to add another, other key to cancel: "))

            print("\n")

            if (again.lower() == "y"):
                pass
            elif (again.lower() != "y"):
                print("____________________")
                break

        #File creation for hospitals.txt
        with open ("hospitals.txt", "x") as hospitalFile:
            hospitalFile.close()

        print("Please insert Hospital Detail (At least 2 and at most 4 hospital can be store in database)\n")

        for x in range(0, 4):
            hospitalCode = input("Hospital Code: ")
            hospitalName = input("Hospital Name: ")
            hospitalLocation = input("Hospital Location: ")

            with open ("hospitals.txt", "at") as hospitalFile:
                line = hospitalCode + "," + hospitalName + "," + hospitalLocation + "\n"
                hospitalFile.write(line)
                hospitalFile.close()

            again = (input("\nDo you want to key in another hospital? Press (Y) to add another, other key to cancel: "))

            print("\n")

            if (again.lower() == "y"):
                pass
            elif (again.lower() != "y"):
                print("____________________")
                break

        #File creation for ppe.txt
        with open ("ppe.txt","x") as ppeFile:
            ppeFile.close()

        while True:
            print("Initial Item Detail\n")

            itemCode = input("Item Code: ")
            itemName = input("Item Name: ")
            supplierCode = input("Supplier code: ")

            with open ("ppe.txt", "at") as ppeFile:
                line = itemCode + "," + itemName + ",100," + supplierCode  + "\n"
                ppeFile.write(line)
                ppeFile.close()

            date = datetime.datetime.now()

            with open ("transactions.txt", "at") as transactionFile:
                line = date.strftime("%x %X") + "," + itemCode + "," + "100," + supplierCode + "\n"
                transactionFile.write(line)
                transactionFile.close()

            again = (input("\nDo you want to key in another item? Press (Y) to add another, other key to cancel: "))

            if (again.lower() == "y"):
                pass
            elif (again.lower() != "y"):
                print("____________________")
                break

        #File creation for usres.txt and also a super user (admin)
        with open("users.txt", "x") as userFile:
            print("Creating an admin...\n")

        while True:
            newAdminUsername = input("Admin username: ")
            newAdminPassword = input("Admin password: ")

            confirm = input("\nPress (Y) to confirm, other key to cancel: ")

            if (confirm.lower() == "y"):
                with open("users.txt", "wt") as userFile:
                    line = newAdminUsername + "," + newAdminPassword + "," + "A\n"
                    userFile.write(line)
                    userFile.close()
                    print("____________________")
                    break
            else:
                pass
        
        print("Initialization completed... All files have been created\n")
        print("Admin username: " + newAdminUsername)
        print("Admin password: " + newAdminPassword)
    except:
        pass

#Login
def login():
    with open("users.txt", "r") as loginFile:
        db = [[str(n) for n in line.strip().split(",")] for line in loginFile.readlines() if line.strip()]

    loginStat = False
    
    print("\nPPE Inventory Mangement System\n")
    
    username = str(input("Username: "))
    password = str(input("Password: "))

    #Checking user
    for x in range(0, len(db)):
        if (username == db[x][0] and password == db[x][1]):
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
        print("\nIncorrect password or username. Please try again or contact admin for assistant!")

#Admin main menu
def adminMainMenu():
    while True:
        print("\nWelcome to PPE Inventory Management System\n")
        print("1. Inventory")
        print("2. Supplier")
        print("3. Hospital")
        print("4. Transaction")
        print("5. Users")
        print("6. Logout")

        print("=========================")
        option = input("Please selct an option: ")
        print("=========================")
        
        admin = True

        if (option == "1"):
            inventory(admin)
        elif (option == "2"):
            suppliers(admin)
        elif (option == "3"):
            hospitals(admin)
        elif (option == "4"):
            transaction(admin)
        elif (option == "5"):
            users()
        elif (option == "6"):
            login()
        else:
            print("\nThere is no such option")

#Main menu
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
        print("=========================")
        
        admin = False

        if (option == "1"):
            inventory(admin)
        elif (option == "2"):
            suppliers(admin)
        elif (option == "3"):
            hospitals(admin)
        elif (option == "4"):
            transaction(admin)
        elif (option == "5"):
            login()
        else:
            print("\nThere is no such option")

#Inventory function
def inventory(admin):
    while True:
        #Make line in ppe.txt become a nested list
        with open("ppe.txt", "r") as ppeFile:
            ppeDB = [[str(n) for n in line.strip().split(",")] for line in ppeFile.readlines() if line.strip()]

        with open("hospitals.txt", "r") as hospitalFile:
            hospitalDB = [[str(n) for n in line.strip().split(",")] for line in hospitalFile.readlines() if line.strip()]

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

            print("1.All item")
            print("2.Selected item")
            print("3.Item with lest then 25")
            print("4.Back")

            print("===============")
            viewOption = input("Select an option: ")
            print("===============")

            #All inventory
            if (viewOption == "1"):
                print("________________________________________________________________")
                print("|{:^15}|{:^15}|{:^10}|{:^20}|".format("Item Code", "Item Name", "Quantity", "Supplier Code"))
                print("|---------------------------------------------------------------|")
                for x in range(len(ppeDB)):
                    print("|{:^15}|{:^15}|{:^10}|{:^20}|".format(ppeDB[x][0], ppeDB[x][1], ppeDB[x][2], ppeDB[x][3]))
                print("|_______________________________________________________________|")

            #An item inventory
            elif (viewOption == "2"):
                itemCode = input("\nItem code: ")

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
                    print("________________________________________________________________")
                    print("|{:^15}|{:^15}|{:^10}|{:^20}|".format("Item Code", "Item Name", "Quantity", "Supplier Code"))
                    print("|---------------------------------------------------------------|")
                    print("|{:^15}|{:^15}|{:^10}|{:^20}|".format(ppeDB[key][0], ppeDB[key][1], ppeDB[key][2], ppeDB[key][3]))
                    print("|_______________________________________________________________|")
                else:
                    print("\nInvalid item code")
                    print("____________________")
            
            #Item with lest than 25
            elif (viewOption == "3"):
                view = []

                #Search for item with less than 25
                for x in range(0, len(ppeDB)):
                    if (int(ppeDB[x][2]) <= 25):
                        view.append(ppeDB[x])
                    else:
                        pass

                print("________________________________________________________________")
                print("|{:^15}|{:^15}|{:^10}|{:^20}|".format("Item Code", "Item Name", "Quantity", "Supplier Code"))
                print("|---------------------------------------------------------------|")
                for x in range(0, len(view)):
                    print("|{:^15}|{:^15}|{:^10}|{:^20}|".format(view[x][0], view[x][1], view[x][2], view[x][3]))
                print("|_______________________________________________________________|") 

            #Back
            elif (viewOption == "4"):
                inventory(admin)

            else:
                print("Invalid option, please try again")
                print("____________________")

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
                print("Supplier Code: " + ppeDB[key][3])

                total = int(ppeDB[key][2]) + int(itemQuantity)
                print("\nQuantity after adding: " + str(total))

                confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                if (confirm.lower() == "y"):
                    ppeDB[key][2] = total

                    #Write into ppe.txt
                    with open("ppe.txt", "wt") as ppeFile:
                        for x in range(len(ppeDB)):
                            line = "{},{},{},{}\n".format(ppeDB[x][0], ppeDB[x][1], ppeDB[x][2], ppeDB[x][3])
                            ppeFile.write(line)

                    #Write transaction into transactions.txt
                    date = datetime.datetime.now()

                    with open ("transactions.txt", "at") as transactionFile:
                        line = date.strftime("%x %X") + "," + itemCode + "," + itemQuantity + "," + ppeDB[key][3] + "\n"
                        transactionFile.write(line)
                        transactionFile.close()
                    
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
                hospitalCode = input("Distributing hospital code: ")

                for y in range(0, len(hospitalDB)):
                    if (hospitalCode == hospitalDB[y][0]):
                        hospitalSearch = hospitalDB[y][0]
                        hospitalKey = y
                        break
                    else:
                        hospitalSearch = hospitalDB[y][0]
                        pass

                if (hospitalSearch == hospitalCode):
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
                                line = "{},{},{},{}\n".format(ppeDB[x][0], ppeDB[x][1], ppeDB[x][2], ppeDB[x][3])
                                ppeFile.write(line)

                        #Write transaction into transactions.txt
                        date = datetime.datetime.now()

                        with open ("transactions.txt", "at") as transactionFile:
                            line = date.strftime("%x %X") + "," + itemCode + ",-" + itemQuantity + "," + hospitalCode + "\n"
                            transactionFile.write(line)
                            transactionFile.close()
                        
                        print("\nOperation successful")
                        print("____________________")
                    else:
                        print("\nOperation canceled")
                        print("____________________")
                else:
                    print("\nInvalid hospital code")
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

#Supplier function
def suppliers(admin):
    while True:
        #Make line in suppliers.txt become a nested list
        with open("suppliers.txt", "r") as suppliersFile:
            suppliersDB = [[str(n) for n in line.strip().split(",")] for line in suppliersFile.readlines() if line.strip()]

        print("\nPPE Supplier Management\n")

        print("1. View Supplier")
        print("2. Add Supplier")
        print("3. Edit Supplier")
        print("4. Delete Supplier")
        print("5. Back")

        print("===============")
        option = input("Select an option: ")
        print("===============")

        #Viewving suppliers-----------------------------------------------------------------------
        if (option == "1"):
            print("\nViewing suppliers...\n")

            print("_____________________________________________________")
            print("|{:^15}|{:^15}|{:^20}|".format("Supplier Code", "Supplier Name", "Supplier Location"))
            print("|----------------------------------------------------|")
            for x in range(len(suppliersDB)):
                print("|{:^15}|{:^15}|{:^20}|".format(suppliersDB[x][0], suppliersDB[x][1], suppliersDB[x][2]))
            print("|____________________________________________________|")


        #Adding suppliers-----------------------------------------------------------------------
        elif (option == "2"):
            print("\nAdding suppliers...\n")

            #Check if there is more than 4 records
            if (len(suppliersDB) < 4):
                newSupplierCode = input("New supplier code: ")

                #Search for duplicate
                for x in range(0, len(suppliersDB)):
                    if (newSupplierCode == suppliersDB[x][0]):
                        dupe = True
                        print("\nSupplier code " + suppliersDB[x][0] + " is already in database, please try again")
                        break
                    else:
                        dupe = False
                    
                if (dupe == True):
                    break
                else:
                    newSupplierName = input("New supplier name: ")
                    newSupplierLocation = input("New supplier Location: ")

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                    if (confirm.lower() == "y"):
                        #Append into suppliers.txt
                        with open("suppliers.txt", "at") as suppliersFile:
                            line = "{},{},{}\n".format(newSupplierCode, newSupplierName, newSupplierLocation)
                            suppliersFile.write(line)

                        print("\nOperation successful")
                        print("____________________")
                    else:
                        print("\nOperation canceled")
                        print("____________________")
            else:
                print("\nOnly 4 suppliers can be store in database")
                print("____________________")

        #Edit suppliers-----------------------------------------------------------------------
        elif (option == "3"):
            print("\nEditing suppliers...\n")
                
            editSupplierCode = input("Supplier code: ")

            #Search for supplier code
            for x in range(0, len(suppliersDB)):
                if (editSupplierCode == suppliersDB[x][0]):
                    search = suppliersDB[x][0]
                    key = x
                    break
                else:
                    search = suppliersDB[x][0]
                    pass

            if (search == editSupplierCode):
                print("\nCurrent supplier code: " + suppliersDB[key][0])
                print("Current supplier name: " + suppliersDB[key][1])
                print("Current supplier location: " + suppliersDB[key][2])

                newSupplierCode = input("\nNew supplier code:")

            #Check if the new code is taken or not
                for x in range(0, len(suppliersDB)):
                    if (newSupplierCode == suppliersDB[x][0]):
                        sameCode = True

                        print("\nSupplier code " + suppliersDB[x][0] + " is already in databse, do you want to rewrite it?")
                        rewrite = input("Press (Y) to confirm, other key to cancel: ")

                        if (rewrite.lower() == "y"):
                            sameCode = False
                        else:
                            pass
                        break
                    else:
                        sameCode = False
                        pass

                if (sameCode == True):
                    print("\nSupplier code " + suppliersDB[x][0] + " is already in database, please try again")
                    print("____________________")
                    pass
                else:
                    newSupplierName = input("New supplier name: ")
                    newSupplierLocation = input("New supplier location: ")

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                    if (confirm.lower() == "y"):
                        suppliersDB[key][0] = newSupplierCode
                        suppliersDB[key][1] = newSupplierName
                        suppliersDB[key][2] = newSupplierLocation

                        #Write into suppliers.txt
                        with open("suppliers.txt", "wt") as suppliersFile:
                            for x in range(0, len(suppliersDB)):
                                line = "{},{},{}\n".format(suppliersDB[x][0], suppliersDB[x][1], suppliersDB[x][2])
                                suppliersFile.write(line)

                        print("\nOperation successful")
                        print("____________________")
                    else:
                        print("\nOperation canceled")
                        print("____________________")
            else:
                print("\nSupplier code is not in database, please try again")
                print("____________________")
                    
        #Deleting suppliers-----------------------------------------------------------------------
        elif (option == "4"):
            print("\nDeleting supplier...")

            if (len(suppliersDB) > 2):
                deleteSupplierCode = input("\nSupplier code: ")

                for x in range(0, len(suppliersDB)):
                    if (deleteSupplierCode == suppliersDB[x][0]):
                        search = suppliersDB[x][0]
                        key = x
                        break
                    else:
                        search = suppliersDB[x][0]
                        key = x
                        pass
                
                if (search != deleteSupplierCode):
                    confirm = "NULL"
                else:
                    print("\nAre you really sure you want to delete " + search + " from database")

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                #If true, pop the inputted supplier
                if (confirm.lower() == "y"):
                    del suppliersDB[key]
                
                    #Write into suppliers.txt
                    with open("suppliers.txt", "wt") as suppliersFile:
                        for x in range(len(suppliersDB)):
                            line = "{},{},{}\n".format(suppliersDB[x][0], suppliersDB[x][1], suppliersDB[x][2])
                            suppliersFile.write(line)

                    print("\nOperation successful")
                    print("____________________")
                elif (confirm == "NULL"):
                    print("\nSupplier code is not in database, please try again")
                    print("____________________")
                else:
                    print("\nOperation canceled")
                    print("____________________")
            else:
                print("\nAt least 2 hospitals must be store in database")
                print("____________________")
            
        #Back-----------------------------------------------------------------------
        elif (option == "5"):
            if admin:
                adminMainMenu()
            else:
                mainMenu()
        else:
            print("\nInvalid option, please try again")
            print("____________________")
    
    suppliersFile.close()

#Hospital function
def hospitals(admin):
    while True:
        #Make line in hospitals.txt become a nested list
        with open("hospitals.txt", "r") as hospitalsFile:
            hospitalsDB = [[str(n) for n in line.strip().split(",")] for line in hospitalsFile.readlines() if line.strip()]

        print("\nPPE Hospital Management\n")

        print("1. View Hospital")
        print("2. Add Hospital")
        print("3. Edit Hospital")
        print("4. Delete Hospital")
        print("5. Back")

        print("===============")
        option = input("Select an option: ")
        print("===============")

        #Viewving hospitals-----------------------------------------------------------------------
        if (option == "1"):
            print("\nViewing hospitals...\n")
            print("_____________________________________________________")
            print("|{:^15}|{:^15}|{:^20}|".format("Hospital Code", "Hospital Name", "Hospital Location"))
            print("|----------------------------------------------------|")
            for x in range(len(hospitalsDB)):
                print("|{:^15}|{:^15}|{:^20}|".format(hospitalsDB[x][0], hospitalsDB[x][1], hospitalsDB[x][2]))
            print("|____________________________________________________|")

        #Adding hospitals-----------------------------------------------------------------------
        elif (option == "2"):
            print("\nAdding hospitals...\n")

            #Check if there is more than 4 records
            if (len(hospitalsDB) > 4):
                newHospitalCode = input("New hospital code: ")

                #Search for duplicate
                for x in range(0, len(hospitalsDB)):
                    if (newHospitalCode == hospitalsDB[x][0]):
                        dupe = True
                        print("\nHospital code " + hospitalsDB[x][0] + " is already in database, please try again")
                        break
                    else:
                        dupe = False
                    
                if (dupe == True):
                    break
                else:
                    newHospitalName = input("New hospital name: ")
                    newHospitalLocation = input("New hospital Location: ")

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                    if (confirm.lower() == "y"):
                        #Append into hospitals.txt
                        with open("hospitals.txt", "at") as hospitalsFile:
                            line = "{},{},{}\n".format(newHospitalCode, newHospitalName, newHospitalLocation)
                            hospitalsFile.write(line)

                        print("\nOperation successful")
                        print("____________________")
                    else:
                        print("\nOperation canceled")
                        print("____________________")
            else:
                print("\nOnly 4 hospitals can be store in database")
                print("____________________")

        #Edit hospitals-----------------------------------------------------------------------
        elif (option == "3"):
            print("\nEditing hospitals...\n")
            
            editHospitalCode = input("Hospital code: ")

            #Search for hospital code
            for x in range(0, len(hospitalsDB)):
                if (editHospitalCode == hospitalsDB[x][0]):
                    search = hospitalsDB[x][0]
                    key = x
                    break
                else:
                    search = hospitalsDB[x][0]
                    pass

            if (search == editHospitalCode):
                print("\nCurrent hospital code: " + hospitalsDB[key][0])
                print("Current hospital name: " + hospitalsDB[key][1])
                print("Current hospital location: " + hospitalsDB[key][2])

                newHospitalCode = input("\nNew hospital code:")

                #Check if the new code is taken or not
                for x in range(0, len(hospitalsDB)):
                    if (newHospitalCode == hospitalsDB[x][0]):
                        sameCode = True

                        print("\nHospital code " + hospitalsDB[x][0] + " is already in databse, do you want to rewrite it?")
                        rewrite = input("Press (Y) to confirm, other key to cancel: ")

                        if (rewrite.lower() == "y"):
                            sameCode = False
                        else:
                            pass
                        break
                    else:
                        sameCode = False
                        pass

                if (sameCode == True):
                    print("\nHospital code " + hospitalsDB[x][0] + " is already in database, please try again")
                    print("____________________")
                    pass
                else:
                    newHospitalName = input("New hospital name: ")
                    newHospitalLocation = input("New hospital location: ")

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                    if (confirm.lower() == "y"):
                        hospitalsDB[key][0] = newHospitalCode
                        hospitalsDB[key][1] = newHospitalName
                        hospitalsDB[key][2] = newHospitalLocation

                        #Write into hospitals.txt
                        with open("hospitals.txt", "wt") as hospitalsFile:
                            for x in range(0, len(hospitalsDB)):
                                line = "{},{},{}\n".format(hospitalsDB[x][0], hospitalsDB[x][1], hospitalsDB[x][2])
                                hospitalsFile.write(line)

                        print("\nOperation successful")
                        print("____________________")
                    else:
                        print("\nOperation canceled")
                        print("____________________")
            else:
                print("\nHospital code is not in database, please try again")
                print("____________________") 
                    

        #Deleting hospitals-----------------------------------------------------------------------
        elif (option == "4"):
            print("\nDeleting hospital...")

            if (len(hospitalsDB) > 2):
                deleteHospitalCode = input("\nHospital code: ")

                for x in range(0, len(hospitalsDB)):
                    if (deleteHospitalCode == hospitalsDB[x][0]):
                        search = hospitalsDB[x][0]
                        key = x
                        break
                    else:
                        search = hospitalsDB[x][0]
                        key = x
                        pass
                
                if (search != deleteHospitalCode):
                    confirm = "NULL"
                else:
                    print("\nAre you really sure you want to delete " + search + " from database")

                    confirm = input("\nPress (Y) to confirm, other key to cancel: ")

                #If true, pop the inputted hospital
                if (confirm.lower() == "y"):
                    del hospitalsDB[key]
                
                    #Write into hospitals.txt
                    with open("hospitals.txt", "wt") as hospitalsFile:
                        for x in range(len(hospitalsDB)):
                            line = "{},{},{}\n".format(hospitalsDB[x][0], hospitalsDB[x][1], hospitalsDB[x][2])
                            hospitalsFile.write(line)

                    print("\nOperation successful")
                    print("____________________")
                elif (confirm == "NULL"):
                    print("\nHospital code is not in database, please try again")
                    print("____________________")
                else:
                    print("\nOperation canceled")
                    print("____________________")
            else:
                print("\nAt least 2 hospitals must be store in database")
                print("____________________")
            
        #Back-----------------------------------------------------------------------
        elif (option == "5"):
            if admin:
                adminMainMenu()
            else:
                mainMenu()
        else:
            print("\nInvalid option, please try again")
            print("____________________")
    
    hospitalsFile.close()

#Transaction function
def transaction(admin):
    while True:
        with open("transactions.txt", "r") as transactionFile:
            transactionDB = [[str(n) for n in line.strip().split(",")] for line in transactionFile.readlines() if line.strip]

        with open("suppliers.txt", "r") as supplierFile:
            supplierDB = [[str(n) for n in line.strip().split(",")] for line in supplierFile.readlines() if line.strip]

        with open("hospitals.txt", "r") as hospitalFile:
            hospitalDB = [[str(n) for n in line.strip().split(",")] for line in hospitalFile.readlines() if line.strip]

        print("\nPPE Transaction History Management\n")

        print("1. View All Transaction")
        print("2. View All Transaction (Add)")
        print("3. View All Transaction (Distribute)")
        print("4. Back")

        print("===============")
        option = input("Select an option: ")
        print("===============")

        #Viewing All Transaction-----------------------------------------------------------------------
        if (option == "1"):
            print("____________________________________________________________________________________")
            print("|{:^25}|{:^15}|{:^15}|{:^25}|".format("Date and Time", "Item Code", "Quantity", "Supplier / Hospital"))
            print("|-----------------------------------------------------------------------------------|")
            for x in range(len(transactionDB)):
                print("|{:^25}|{:^15}|{:^15}|{:^25}|".format(transactionDB[x][0], transactionDB[x][1], transactionDB[x][2], transactionDB[x][3]))
            print("|___________________________________________________________________________________|")
        
        #Viewing All Add Transaction-----------------------------------------------------------------------
        elif (option == "2"):
            view = []

            #Search for inventory distributing transaction
            for x in range (len(transactionDB)):
                for y in range (len(supplierDB)):
                    if (transactionDB[x][3] == supplierDB[y][0]):
                        temp = [transactionDB[x][0], transactionDB[x][1], transactionDB[x][2], transactionDB[x][3]]
                        view.append(temp)

            print("_______________________________________________________________________________")
            print("|{:^25}|{:^15}|{:^15}|{:^20}|".format("Date and Time", "Item Code", "Quantity", "Supplier"))
            print("|------------------------------------------------------------------------------|")
            for x in range(len(view)):
                print("|{:^25}|{:^15}|{:^15}|{:^20}|".format(view[x][0], view[x][1], view[x][2], view[x][3]))
            print("|______________________________________________________________________________|")

        #View All Dustribute Transaction-----------------------------------------------------------------------
        elif (option == "3"):
            view = []

            #Search for inventory adding transaction
            for x in range(len(transactionDB)):
                for y in range(len(hospitalDB)):
                    if (transactionDB[x][3] == hospitalDB[y][0]):
                        temp = [transactionDB[x][0], transactionDB[x][1], transactionDB[x][2], transactionDB[x][3]]
                        view.append(temp)

            print("_______________________________________________________________________________")
            print("|{:^25}|{:^15}|{:^15}|{:^20}|".format("Date and Time", "Item Code", "Quantity", "Hospital"))
            print("|------------------------------------------------------------------------------|")
            for x in range(len(view)):
                print("|{:^25}|{:^15}|{:^15}|{:^20}|".format(view[x][0], view[x][1], view[x][2], view[x][3]))
            print("|______________________________________________________________________________|")

        #Back-----------------------------------------------------------------------
        elif (option == "4"):
            if admin:
                adminMainMenu()
            else:
                mainMenu()
        else:
            print("Invalid option, please try again")
            print("____________________")

#Admin users function
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

        #Viewing Users-----------------------------------------------------------------------
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

            #Search for duplicate
            for x in range(0, len(usersDB)):
                if (newUser == usersDB[x][0]):
                    dupe = True
                    print("\nUsername " + usersDB[x][0] + " has been taken, please try again")
                    break
                else:
                    dupe = False
            
            if (dupe == True):
                break
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
            
            if (search != deleteUser):
                confirm = "NULL"
            else:
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
            elif (confirm == "NULL"):
                print("\nUsername cant be found database, please try again")
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
    initial()
    login()