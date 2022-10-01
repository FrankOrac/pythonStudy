#Custom Generator Function

def customgen(x,y):

    while (x<y):
        yield x
        x+=2
        #print(x)

# Now let's invoke the function
a=customgen(23,90)
for number in a:
    print(number)