#Reduction Function
from functools import reduce
a = [1,2,3,4,5,6,7,8]
print(reduce(lambda x,y:x+y, a))
print(reduce(lambda x,y:x-x, a))
print(reduce(lambda x,y :x*y, a))
