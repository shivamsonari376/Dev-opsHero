def check_password_strength(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)

    if (length < 8):
        print("Password not valid")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1

    if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            print("Valid Password\n")
        else:
            print("Password not valid\n")
    else:
        if (upperChars == 0):
            print("Password not valid\n")
        if (lowerChars == 0):
            print("Password not valid\n")
        if (specialChars == 0):
            print("Password not valid\n")
        if (digits == 0):
            print("Password not valid\n")


password = input("Please enter password: ")
check_password_strength(password)
