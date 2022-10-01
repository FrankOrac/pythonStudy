def dr(no=int(input("Enter a  number"))):
   # no = int(input("enter a number"))
    try:

        value = 5/no

    except ZeroDivisionError:
        print("zero error", value)
        value =1
        return 1