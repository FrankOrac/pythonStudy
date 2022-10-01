#ASSIGNMENT
#Write a score algorithm program in python
# all rights Reserved. Frank Craig  ⓒ2022
#Proper documentation by Frank

#using the while loop statement
Version ="v2.0"
print("WELCOME TO SCORE ALGORITHM ", Version , "\t", "Created by Frank Orac with",  "\U0001f600")
while True:
    #using the catch exception to try if strings or special characters are enterred
    try:

       #gets the input from the user and store it as grade in integer format
        frankDefGrade = int(input("What was your score?  "))
       #conditional statement to flag error message when user inputs value greater than 100
        if frankDefGrade >= 101 :

            print("Grading can not be greater than 100", "You are getting this error because your input was", frankDefGrade)
            continue
        elif frankDefGrade<0:
            print("Score can not be a negative number")
            continue


           #this exception prints error message when user input strings or special characters
    except ValueError:
        print("Incorrect input", "\n","\t", "Note:-" ,"\n", "Decimal numbers, Strings and special charaters not allowed in grading system" )
#this continues the loop after the error message
        continue
    else:

#this breaks the  loop statement if input is true
        break
        #compare the user's input stored as grade with each defined grade
if frankDefGrade >= 70 and frankDefGrade <= 100: #GRADE A
    print("Your grade is A because you scored ", frankDefGrade, "\n", "\t", "You have beeen awarded a scholarship")
elif frankDefGrade >= 59 and frankDefGrade <= 69: #Grade B
    print("Your grade is B because you scored ", frankDefGrade, "\n", "\t", "You just won a paid trip to Oluku")
elif frankDefGrade >= 49 and frankDefGrade <= 58: #Grade c
    print("Your grade is C because you scored ", frankDefGrade, "\n", "\t", "You just won a cold bottle of zobo")
elif frankDefGrade >= 39 and frankDefGrade <= 48: #Grade D
    print("Your grade is D because you scored ", frankDefGrade, "\n", "\t", "You just won a cold bottle of zobo")

elif frankDefGrade >= 0 and frankDefGrade <= 38: #Grade F
    print("Your grade is F because you scored ", frankDefGrade, "\n", "\t", "Tears", "\U0001f600", "\U0001F923", "\U0001F923", "\U0001F61B" )


#written with love by Frank Orac
# all rights Reserved. Frank Orac  ⓒ2022