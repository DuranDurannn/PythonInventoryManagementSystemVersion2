START inventory(admin)
    WHILE TRUE
        READ "ppe.txt" AS ppeDB[][]
        READ "hospital.txt" AS hospitalDB[][]

        READ (option)

        #View inventory
        IF (option == 1)
            #View all item
            IF (viewOption == 1)
                FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                    DISPLAY ppeDB[x]
                END FOR
            #View an item
            ELSE IF (viewOption == 2)
                READ (itemCode)

                FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                    IF (itemcode == ppeDB[x][0])
                        search = ppeDB[x][0]
                        key = x
                        BREAK
                    ELSE IF 
                        PASS
                    END IF
                END FOR
                
                DISPLAY ppeDB[x]
            #View item with less than 25 unit
            ELSE IF (viewOption == 3)
                view = []

                FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                    IF (ppeDB[x][2] <= 25) 
                        APPEND ppeDB[x] TO view[]
                    ELSE
                        PASS
                    END IF
                END FOR

                FOR x FROM 0 TO LENGTH OF view[] STEP 1
                    DISPLAY view[x]
                END FOR
            ELSE IF (viewOption == "5")
                inventory(admin)
            ELSE
                DISPLAY ("Invalid Option")
            END IF
        
        #Adding Inventory
        ELSE IF (option == "2")
            READ (itemCode)
            
            FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                IF (itemcode == ppeDB[x][0])
                    search = ppeDB[x][0]
                    key = x
                    BREAK
                ELSE IF 
                    PASS
                END IF
            END FOR        
                
                IF (search == itemCode)
                    READ itemQuantity

                    total = ppeDB[key][2] + itemQuantity

                    READ confirm

                    IF (confirm == "y")
                        FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                            OPRM "ppe.txt"
                                WRITE ppeDB[x]
                        END FOR

                        OP#N "transaction.txt"
                            APPEND date + "," + itemCode + "," + itemQuantity + "," + ppeDB[key][3] + "\n"

                        DISPLAY ("Operation successful")       
                    ELSE
                        DISPLAY ("Operation canceled")
                    END IF
                ELSE
                    DISPLAY ("Invalid item code")
                END IF

        #Distributing inventory
        ELSE IF (option == "3")
            READ (itemCode)
            
            FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                IF (itemcode == ppeDB[x][0])
                    search = ppeDB[x][0]
                    key = x
                    BREAK
                ELSE IF 
                    PASS
                END IF
            END FOR

            IF (search == itemCode)
                DISPLAY ("Current quantity: " + ppeDB[key][2])
            
                READ itemQuantity
                READ hospitalCode

                FOR Y FROM 0 TO LENGTH OF hospitalDB[] STEP 1
                    IF (itemcode == hospitalDB[y][0])
                        hospitalSearch = hospitalDB[y][0]
                        hospitalKey = y
                        BREAK
                    ELSE IF 
                        PASS
                    END IF
                END FOR

                IF (hospitalSearch == hospitalCode)
                    IF (ppeDB[key][2] >= itemQuantity)
                        total = ppeDB[key][2] = itemQuantity
                        READ confirm
                    ELSE
                        DISPLAY ("Not enough stock")
                    END IF

                IF (confirm == "y")
                    ppeDB[key][2] = total

                    FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                        OPEN "ppe.txt"
                            WRITE ppeDB[x]
                    END FOR

                    OPEN "transactions.txt"
                        APPEND date + "," + itemCode + "," + itemQuantity + "," + ppeDB[key][3] + "\n"
                        
                    DISPLAY ("Operation successful")
                ELSE
                    DISPLAY ("Operation canceled")
                END IF
            ELSE
                DISPLAY ("Invalid item code")
            END IF

        #Back
        ELSE IF (option == "4")
            IF admin:
                adminMainMenu()
            ELSE
                mainMenu()
            END IF
        ELSE
            DISPLAY ("Invalid option")
        END IF
    WHILE END
END inventory(admin)