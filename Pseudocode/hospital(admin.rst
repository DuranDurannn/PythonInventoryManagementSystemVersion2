START hospital(admin)
    WHILE TRUE
        OPEN "hospital.txt" AS hospitalsDB[][]

        READ (option)

        #View all hospital
        IF (option == "1")
            FOR x FROM 0 TO LENGTH OF hospitalsDB[] STEP 1
                DISPLAY hospitalsDB[x]
            END FOR

        #Adding hospital    
        ELSE IF (option == "2")
            READ (newHospitalCode)

            FOR x FROM 0 TO LENGTH OF hospitalsDB[] STEP 1
                IF (newHospitalCode == hospitalsDB[x][0])
                    dupe = TRUE
                    BREAK
                ELSE
                    dupe = FALSE
                END IF
            END FOR

            IF (dupe == True)
                BREAK
            ELSE
                READ (newHospitalName)
                READ (newHospitalLocation)

                READ (confirm)

                IF (comfirm == "y")
                    OPEN "hospital.txt"
                        APPEND newHospitalCode + "," + newHospitalName + "," + newHospitalLocation  + "\n"

                    DISPLAY "Operation successful"
                ELSE
                    DISPLAY "Operation canceled"
                END IF

        #Editing hospital
        ELSE IF (option == "3")
            READ (editHospitalCode)

            FOR x FROM 0 TO LENGTH OF hospitalsDB[] STEP 1
                IF (editHospitalCode == hospitalsDB[x][0])
                    search = hospitalsDB[x][0]                        key = x
                    BREAK
                ELSE
                    PASS
                END IF
            END FOR

            IF (search == editHospitalCode)
                DISPLAY ("Current hospital code: " + hospitalsDB[key][0])
                DISPLAY ("Current hospital name: " + hospitalsDB[key][1])
                DISPLAY ("Current hospital location: " + hospitalsDB[key][2])

                READ (newHospitalCode)

                FOR x FROM 0 TO LENGTH OF hospitalsDB[] STEP 1
                    IF (newHospitalCode == hospitalsDB)
                        saneCode = TRUE

                        READ (rewrite)

                        IF (rewrite == "y")
                            sameCode = FALSE
                        ELSE
                            PASS
                        END IF
                    ELSE
                        sameCode = FALSE
                    END IF
                END FOR

                IF (sameCode == TRUE)
                    DISPLAY ("Hospital is in database")
                ELSE
                    READ (newHospitalName)
                    READ (newHospitalLocation)

                    READ (confirm)

                    IF (confirm == "y")
                        hospitalsDB[key][0] = newHospitalCode
                        hospitalsDB[key][1] = newHospitalName
                        hospitalsDB[key][2] = newHospitalLocation
                            
                        OPEN "hospital.txt"
                            FOR x FROM 0 TO LENGTH OF hospitalsDB[] STEP 1
                                WRITE hospitalDB[x]
                            END FOR

                        DISPLAY ("Operation successful")
                    ELSE
                        DISPLAY ("Operation canceled")
                    END IF
            ELSE
                DISPLAY ("Hospital code not in database")      
            END IF
            
        #Deleting hospital
        ELSE IF (option == "4")
            READ (deleteHospitalCode)

            FOR x FROM 0 TO LENGTH OF hospitalDB[] STEP 1
                IF (deleteHospitalCode == hospitalDB[x][0])
                    search = hospitalsDB[x][0]
                    key = x
                    BREAK
                ELSE
                    PASS
                END IF
            END FOR

            IF (search != deleteHospitalCode)
                confirm = "NULL"
            ELSE
                READ (confirm)
            END IF

            IF (confirm == "y")
                DELETE hospitalDB[key]

                OPEN "hospital.txt" 
                    FOR x FROM 0 TO LENGTH OF hospitalDB[] STEP 1
                        WRITE hospitalsDB[x]
                    END FOR
                        
                DISPLAY ("Operation successful")
            ELSE
                DISPLAY("Hospital code is not in database")
            END IF

        #Back
        ELSE IF (option == 5)
            IF (admin == TRUE)
                adminMainMenu()
            ELSE
                mainMenu()
            END IF
        END IF
    WHILE END
END hospital(admin)