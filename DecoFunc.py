#DeCORATOR functions

def decore(fun):
    def inner():
        result = fun()
        return result * 4
    return inner

# Now let's invoke the function

def num():
    return 9

resultfun = decore(num)
print(resultfun())


