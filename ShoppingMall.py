##using a while loop statement for a voters algorithm
def AgeCalc():
    print("welcome to DIAMOND Shooppng Mall ")
    print("to Sign Up an account , Enter the following details properly")
    while True:
        try:
            PhoneNumber = int(input("PLEASE ENTER YOUR PHONE NUMBER"))
            if PhoneNumber == None:
                print("iNVALID")
                continue
            elif PhoneNumber is not True:
                print("You are too young to vo")
                break
        except ValueError:
            print("")
            return 