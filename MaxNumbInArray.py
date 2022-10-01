#Maximum numb in array

max= None
a = [1,2,3,4,5,6,7,8,9]
for num in a:
    if max is None or num>max:
        max=num
        print('maximum number is' , max)
       # break