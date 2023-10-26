START adminMainMenu()
    WHILE TRUE 
        READ option

        admin = TRUE

        IF (OPTION == 1)
            inventory(admin)
        ELSE IF (OPTION == 2)
            suppliers(admin)
        ELSE IF (OPTION == 3)
            hospitals(admin)
        ELSE IF (OPTION == 4)
            transaction(admin)
        ELSE IF (OPTION == 5)
            users(admin)
        ELSE IF (OPTION == 6)
            login()
        ELSE
            DISPLAY ("No such option")
        END IF
    END WHILE
END adminMainMenu()

START mainMenu()
    WHILE TRUE 
        READ option

        admin = FALSE

        IF (OPTION == 1)
            inventory(admin)
        ELSE IF (OPTION == 2)
            suppliers(admin)
        ELSE IF (OPTION == 3)
            hospitals(admin)
        ELSE IF (OPTION == 4)
            transaction(admin)
        ELSE IF (OPTION == 5)
            login()
        ELSE
            DISPLAY ("No such option")
        END IF
    END WHILE
END mainMenu()