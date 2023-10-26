START users()
    WHILE TRUE
        OPEN "users.txt" AS usersDB[][]
    
        READ (option)

        #View all users
        IF (option == "1")
            FOR x FROM 0 TO LENGTH OF usersDB[] STEP 1
                DISPLAY usersDB[x]
            END FOR
        
        #Add user
        ELSE IF (option == "2")
            READ (newUser)

            FOR x FROM 0 TO LENGTH OF usersDB[x]
                IF (newUser == usersDB[x][0])
                    dupe = TRUE
                    DISPLAY ("Username has been taken")
                    BREAK
                ELSE
                    dupe = FALSE
                END IF
            
            IF (dupe == TRUE)
                BREAK
            ELSE
                READ (newPassword)
                READ (authority)

                READ (confirm)

                IF (confirm == "y")
                    IF (authority == "a" OR "s")
                        OPEN "users.txt" 
                            APPEND newUser + "," + newPassword + "," + authority  + "\n"

                        DISPLAY ("Operation successful")
                    ELSE
                        DISPLAY ("Invalid authority status")
                    END IF
                ELSE
                    DISPLAY ("Operation canceled")
                END IF
            
        #Edit users
        ELSE IF (option == "3")
            READ (editUser)

            FOR x FROM 0 TO LENGTH OF usersDB[] STEP 1
                IF (edituser == usersDB[x][0])
                    search = usersDB[x][0]
                    key = x
                    BREAK
                ELSE
                    PASS
                END IF
            END FOR
                
            IF (search == editUser)
                DISPLAY ("\nCurrent username: " + usersDB[key][0])
                DISPLAY ("Current password: " + usersDB[key][1])
                DISPLAY ("Current authorization (A / S): " + usersDB[key][2])

                READ (newUsername)
                READ (newPassword)
                READ (newAuthority)

                READ (confirm)

                IF (confirm == "y")
                    usersDB[key][0] = newUsername
                    usersDB[key][1] = newPassword
                    usersDB[key][2] = newAuthority

                    OPRN "users.txt"
                        FOR x FROM 0 TO LENGTH OF usersDB STEP 1
                            WRITE usersDB[x]
                        END FOR
                            
                        DISPLAY ("Operation successful")
                    ELSE
                        DISPLAY ("Operation canceled")
                    END IF
            ELSE
                DISLAY ("Username is not in database")

        #Delete user
        ELSE IF (option == "4")
            READ (deleteUser)

            FOR x FROM 0 TO LENGTH OF usersDB[] STEP 1
                IF (deleteUser == usersDB[x][0])
                    search = usersDB[x][0]
                    key = x
                    BREAK
                ELSE
                    PASS
                END IF
            END FOR

            IF (search != deleteUser)
                confirm = "NULL"
            ELSE
                READ (confirm)
            END IF

            IF (confirm == "y")
                DELETE usersDB[key]

                OPEN "users.txt"
                    FOR x FROM 0 TO LENGTH OF usersDB[] STEP 1
                        WRITE usersDB[]
                    END FOR

                DISPLAY ("Operation successful")
            ELSE IF (confirm == "NULL")
                DISPLAY ("Username cant be found in database")
            ELSE
                DISPLAY ("Operation canceled")
            END IF

        #Back
        ELSE IF (option == "5")
            adminMainMenu
        ELSE
            DISPLAY ("Invalid option")
        END IF
    WHILE END
END users()