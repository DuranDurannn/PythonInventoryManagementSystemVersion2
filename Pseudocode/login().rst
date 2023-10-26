START login()
    READ "users.txt" AS db[]
    
    READ (username)
    READ (password)

    FOR x FROM 0 TO LENGTH OF db[] STEP 1
        IF (username AND password IS IN "users.txt")
            IF (authority == "A")
                adminMainMenu()
                admin = TRUE
            ELSE IF (authority == "S")
                mainMenu()
                admin = FALSE
            END IF
        END IF
    END FOR
END login()