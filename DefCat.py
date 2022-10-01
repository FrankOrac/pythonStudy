while True:
    try:
        a = int(input("enter a number"))
    except ValueError:
        print("Strings not allowed")
        continue

        s = 2
        if a==s:
            print("correct pin")
            break
        else:
            print("error")
