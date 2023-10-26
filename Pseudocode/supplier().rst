START suppliers(admin)
    WHILE TRUE
        OPEN "suppliers.txt" AS suppliersDB[][]
        OPEN "ppe.txt" AS ppeDB[][]

        READ (option)

        #Viwew suppliers
        IF (option == "1")
            FOR x FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                DISPLAY suppliersDB[x]
            END FOR

        #Add suppliers    
        ELSE IF (option == "2")
            READ (newSupplierCode)
            READ (newSupplierName)
            READ (newSupplierLocation)
            READ (newSuppliedItemCode)

            FOR x FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                IF (newSupplierCode == suppliersDB[x][0])
                    dupe = TRUE
                    DISPLAY ("Supplier is in database")
                ELSE IF (newSupplierCode IN suppliersDB[x][3])
                    READ (rewrite)
                    key = x
                    BREAK
                ELSE
                    dupe = FALSE
                END IF

            TRY
                IF (rewrite == "y")
                    temp = suppliersDB[key][3]

                    READ (newInput)
                    newList[] = newInput

                    IF (newList == tempList)
                        suppliersDB[key][3] = "-"
                    END IF
                    
                    OPEN "supplers.txt" 
                        FOR x FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                            WRITE suppliersDB[x]
                        END FOR
            EXCEPT
                dupe = TRUE
                
            IF (dupe == FALSE)
                READ (confirm)

                IF (confirm == "y")
                    OPEN "suppliers.txt"
                        APPEND newSupplierCode + "," + newSupplierName + "," + newSupplierLocation + "," + newSuppliedItemCode + "\n"
                    
                    OPEN "suppliers.txt" AS newSuppliersDB[][]

                    FOR x FROM 0 TO LENGTH OF ppeDB[]
                        FOR y FROM 0 TO LENGTH OF newSuppliersDB[]
                            IF (ppeDB [x][0] IN newSuppliedItemCode)
                                ppeDB[x][3] = newSuppliersDB[y][0]
                            END IF
                        END FOR
                    END FOR

                    FOR x FROM 0 TO LENGTH OF ppeDB[]
                        WRITE ppeDB[x][3]
                    END FOR
                    
                    DISPLAY ("Operation successful")
                ELSE
                    DISPLAY ("Operation canceled")
                END IF
            ELSE
                BREAK
            END IF

        #Edit suppliers
        ELSE IF (option == "3")
            READ (editSupplierCode)

            FOR x FROM 0 TO LENGTH OF newSuppliersDB[] STEP 1
                IF (editSupplierCode == suppliersDB[x][0])
                    search = newSuppliersDB[x][0]
                    key = x
                    BREAK
                ELSE
                    PASS
                END IF
            END FOR

            IF (search == editSupplierCode)
                DISPALY ("Current supplier code: " + suppliersDB[key][0])
                DISPLAY ("Current supplier name: " + suppliersDB[key][1])
                DISPLAY ("Current supplier location: " + suppliersDB[key][2])
                DISPLAY ("Current supplied item code: " + suppliersDB[key][3])

                READ (newSupplierCode)

                FOR x FROM 0 TO LENGTH OF suppliersDB STEP 1
                    IF (newSupplierCode == suppliersDB[x][0])
                        sameCode = TRUE

                        READ (rewrite)

                        IF (rewrite == "y")
                            sameCode = FALSE
                        END IF
                    ELSE
                        sameCode = FALSE
                    END IF
                END FOR

                IF (sameCode == TRUE)
                    DISPLAY ("Supplier code is in database")
                ELSE
                    READ (newSupplierName)
                    READ (newSupplierLocation)
                    READ (newSuppliedItemCode)

                    READ (confirm)

                IF (confirm == "y")
                    suppliersDB[key][0] = newSupplierCode
                    suppliersDB[key][1] = newSupplierName
                    suppliersDB[key][2] = newSupplierLocation
                    suppliersDB[key][3] = newSuppliedItemCode

                    FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                        FOR y FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                            IF (ppeDB[x][0] IN suppliersDB[y][3])
                                ppeDB[x][0] = suppliersDB[y][0]
                            END IF
                        END FOR
                    END FOR

                    OPEN "ppe.txt"
                        FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                            WRITE ppeDB[x]
                        END FOR
                    
                    OPEN "suppliers.txt"
                        FOR x FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                            WRITE suppliersDB[x]
                        END FOR
                    
                    DISPLAY ("Operation successful")
                ELSE
                    DISPLAY ("Operation canceled")
                END IF
            ELSE
                DISPLAY ("Supplier code cant be found")
            END IF
        
        #Deleting suppliers
        ELSE IF (option == "4")
            READ (deleteSupplierCode)

            FOR x FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                IF (deleteSupplierCode == suppliersDB[x][0])
                    search = suppliersDB[x][0]
                    key = x
                    BREAK
                ELSE
                    PASS
                END IF
            END FOR
            
            IF (search != deleteSupplierCode)
                confirm = "NULL"
            ELSE
                READ (confirm)

                IF (confirm == "y")
                    FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                        FOR y FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                            IF (ppeDB[x][0] IN suppliersDB[key])
                                ppeDB[x][3] = "-"
                            END IF
                        END FOR
                    END FOR

                    DELETE suppliers[key]

                    OPEN "ppe.txt"
                        FOR x FROM 0 TO LENGTH OF ppeDB[] STEP 1
                            WRITE ppeDB[x]
                        END FOR

                    OPEN "ppe.txt"
                        FOR x FROM 0 TO LENGTH OF suppliersDB[] STEP 1
                            WRITE suppliersDB[x]
                        END FOR
                    
                    DISPLAY ("Operation successful")
                ELSE
                    DISPLAY ("Operation canceled")
                END IF
            END IF
        
        #Back
        ELSE IF (option == "5")
            IF admin
                adminMainMenu()
            ELSE 
                mainMenu()
            END IF
        ELSE
            DISPLAY ("Invalid option")
        END IF
    END WHILE
END supplers(admin)