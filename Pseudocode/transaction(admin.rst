START transaction(admin)
    WHILE TRUE
        OPEN "transaction.txt" AS transactionDB[][]

        READ (option)

        #View all transaction
        IF (option == "1")
            FOR x FROM 0 TO LENGTH OF transactionDB[] STEP 1
                DISPLAY transactionDB[x]
            END FOR

        #View all adding transaction
        ELSE IF (option == "2")
            view = []

            FOR x FROM 0 TO LENGTH OF +hospitalDB[] STEP 1
                IF (transactionDB[x][2] >= 0)
                    temp = temp = [transactionDB[x][0], transactionDB[x][1], transactionDB[x][2], transactionDB[x][3]]
                    APPEND temp TO view
                END IF
            END FOR

            FOR x FROM 0 TO LENGTH OF view[] STEP 1
                DISPLAY view[x]
            END FOR
        
        #View all distributing transaction
        ELSE IF (option == "3")
            view = []

            FOR x FROM 0 TO LENGTH OF hospitalDB[] STEP 1
                IF (transactionDB[x][2] < 0)
                    temp = temp = [transactionDB[x][0], transactionDB[x][1], transactionDB[x][2], transactionDB[x][3]]
                    APPEND temp TO view
                END IF
            END FOR

            FOR x FROM 0 TO LENGTH OF view[] STEP 1
                DISPLAY view[x]
            END FOR

        #Back
        ELSE IF (option == "4")
            IF (admin == TRUE)
                adminMainMenu()
            ELSE
                mainMenu()
            END IF
        ELSE 
            DISPLAY ("Invalid option")
        END IF
    END WHILE
END transaction(admin) 