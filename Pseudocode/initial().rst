START initial()
  TRY
    CREATE “transaction.txt”
    CREATE “suppliers.txt”

    FOR x FROM 0 TO 4 STEP 1
      READ (supplierCode)
      READ (supplierName)
      READ (supplierLocation)
      READ (supplierItemCode)

      OPEN "suppliers.txt"
        APPEND supplierCode + "," + supplierName + "," + supplierLocation + "," + suppliedItemCode + "\n"

      READ (again)
          
      IF (again == “y”)
        PASS
      ELSE
        BREAK
      END IF
    END FOR

    CREATE “hospitals.txt”
    
    FOR x FROM 0 TO 4 STEP 1
      READ (hospitalCode)
      READ (hospitalName)
      READ (hospitalLocation)

      OPEN “hospitals.txt”
        APPEND hospitalCode + "," + hospitalName + "," + hospitalLocation + “\n”

      READ (again)

      IF (again == “y”)
        PASS
        BEXT STEP
      ELSE
        BREAK
      END IF
    END FOR

    CREATE “suppliers.txt”

    FOR x FROM 0 TO 4 STEP 1
      READ (supplierCode)
      READ (supplierName)
      READ (supplierLocation)
      READ (supplierItemCode)

      OPEN "suppliers.txt"
        APPEND supplierCode + "," + supplierName + "," + supplierLocation + "," + suppliedItemCode + "\n"

      READ (again)
          
      IF (again == “y”)
        PASS
      ELSE
        BREAK
      END IF
    END FOR

    CREATE "ppe.txt"

    WHILE TRUE
      READ (itemCode)
      READ (itemName)
      READ (supplierCode)

      OPEN "ppe.txt"
        APPEND itemCode + "," + itemName + ",100," + supplierCode  + "\n"

      OPEN "transactions.txt"
        APPEND date + "," + itemCode + "," + "100," + supplierCode + "\n"

      READ (again)

      IF (again == “y”)
        PASS
      ELSE
        BREAK
      END IF
    END WHILE

    CREATE "users.txt"

    WHILE TRUE
      READ(newAdminUsername)
      READ(newAdminPassword)

      READ(confirm)

      IF (confirm == "y")
        APPEND newAdminUsername + "," + newAdminPassword + "," + "A\n"
        BREAK
      ELSE
        PASS
      END IF
    END WHILE

  EXCEPT
    PASS
END initial()