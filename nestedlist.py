#writing a nested list

a= [["name", "age" , "travel_history", "state"],
    ("date_of_birth", "LGA", "Occupation", [4,5,6,7,8]),
    [3,45,7, ("HP", "Mackbook", "Find me", ["try findind me"])] ]

#print(a[2][-1][3][0])
#print(len(a[2]))

print(a[2][-1][-1][0]) 