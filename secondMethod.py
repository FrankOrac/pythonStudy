import math


def frankcalc():
    while True:
        try:
            a = int(input("Enter the value of a"))
            b = int(input("Enter th value of b"))
            c = int(input("Enter the value of c"))
            fr = b * b - (4 * a * c)
            frsqr = math.sqrt(abs(fr))

            if fr == 0:
                print("Quadratic does not function with zero")

                continue


            elif fr <= -1:

                print("Real and same roots")
                print(-b / (2 * a))
                break




            elif fr > 0:

                final2 = (-b - frsqr) / (2 * a)
                final1 = (-b + frsqr) / (2 * a)
                print("Real and different roots")
                print("First value is", "\t", final1)
                print("Second value is", "\t", final2)
                break

        except ValueError or ZeroDivisionError:
            print("Invalid Entry Please try AGAIN!")
            continue
            break
            return frankcalc()

        # print("Complex Roots")
        # print(-b / (2 * a), "+ i", frsqr)
        #     print(-b / (2 * a), "-i", frsqr)



# if a == 0:
#   print("Input correct quadractic equation")
# else:
# frankcalc()
