##using a while loop statement for a voters algorithm
#from pip._internal.utils import datetime
#import datetime
#from datetime import datetime


def AgeCalc():
    while True:
        try:
            age = int(input("Please Enter Your age"))
            if age <= 0:
                print("Age can not be a negative number or a Zero")
                continue
            elif age < 18 >= 1:
                print("You are too young to vote")
                continue
            elif age > 70:
                print("You are too old to vote")
                continue
            elif age >= 18 < 70:
                print("You are Eligibe to vote")
                break

        except  ValueError:
            print("NOTE STRINGS, DECIMALS, SPECIAL CHARACTER ARE INVALID in Voters registration")
    return
