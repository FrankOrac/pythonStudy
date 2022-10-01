# Assigment
# Write a program in python to validate sim pin and puk code at a maximum of three tries
# Program written by Frank Orac
#import sys

# This code imports the windows beep sound from the library **Frank Orac
import winsound

# this set duration of the  sound to 250milliseconds **Frank Orac
frankDurat = 500  # milliseconds **Frank Orac
# This sets the sound's frequency to 440hz **Frank Orac
frankfreq = 440  # Hz


# defines the function to verify the sim pin entry
def Vpin(pin):

    # a coditional statement to check if the entered pin is correct
    if pin == 8080:
        return True
    else:
        return False


# a variable initialized to zero to repeat the number of tries
count_input = 0

# a loop to check and repeat the task(input pin )
while count_input <3:  # while the user input is less than 3
    try:
        pin = int(
            input("please enter your sim pin code " ))  # prompt and get user's input and store in pin variable as integer
    except ValueError:
        #  print()
        print("Incorrect input", "\n", "\t", "Strings and special charaters not allowed in Pin Verification system")
        continue

    if Vpin(pin):
        print("Correct, Welcome to Frank Sim Network", "\t", "Created by Frank Orac with", "\U0001f600")

        break

    else:  # repeats task
        print(pin, "is incorrect.Please enter again: ")
        at = 2 - count_input
        print("You Have %s More Attempt Remaining" % at)
    count_input += 1
else:  # blocks the sim card after 3 incorrect tries and plays a  beep sound and prompt user to enter puk code
    print("What type of playing is this", winsound.Beep(frankfreq, frankDurat), winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat), "\U0001F604", )
    print("Your sim card has been blocked", "\n", "\t")
    Puk = int(input("Enter your Puk Code now"))



# defines the function to verify the sim pin entry
def Vpuk(puk):
    # conditional statement for sim puk code verification
    if puk == 34348080:
        return True
    else:
        return False


# a variable initialized to zero to repeat the number of tries
count_input1 = 0

while count_input1 < 3:  # while the user input is less than 3
    try:
        puk = int(
            input("please enter your sim puk code"))  # prompt and get user's input and store in puk variable as integer
    except ValueError:
        print("Incorrect input", "\n", "\t", "Strings and special charaters not allowed in SIM PUK Verification system")
        continue

    if Vpuk(puk):
        print("Correct PuK", "You will reecive a new configuration shortly for pin reset")
        print("WELCOME TO Frank Sim Network ", "\t", "Created by Frank Orac with", "\U0001f600")
        break
    else:
        print("Are you playing ", "\U0001F604", "\t", "\n", puk, "is incorrect.Please enter the correct one again: ")
        at = 2 - count_input1
        print("You Have %s More Attempt Remaining" % at)
    count_input1 += 1
else:

    # displays Your sim card has benn destroyed 😛 None None None None None None None None None None None None None None None None None None 😛 😛 😛 😛 😛 😛
    print("Your sim card has been destroyed completely", "\U0001F61B", winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat)
          , winsound.Beep(frankfreq, frankDurat), winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat)
          , winsound.Beep(frankfreq, frankDurat), winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat)
          , winsound.Beep(frankfreq, frankDurat), winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat)
          , winsound.Beep(frankfreq, frankDurat), winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat),
          winsound.Beep(frankfreq, frankDurat)
          , "\U0001F61B", "\U0001F61B", "\U0001F61B", "\U0001F61B", "\U0001F61B", "\U0001F61B")

# all rights Reserved. Frank Craig  ⓒ2022
