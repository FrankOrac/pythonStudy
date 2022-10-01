#wednesday class work




test_stirng = input("enter your essay : ")
total = 1

for i in range(len(test_stirng)):
   if(test_stirng[i] == ' ' or test_stirng == '\n' or test_stirng == '\t'):
      total = total + 1

print("Total Number of Words in your essay is: ", total)