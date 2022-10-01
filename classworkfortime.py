# write a code to tell a user goodmorning as  long its not yet 12nioon

import datetime

currentTime = datetime.datetime.now()
currentTime.hour
0
if currentTime.hour < 12:
    print('Good morning.')
elif 12 <= currentTime.hour < 18:
  print("Good afternoon")
else:
    print("Good evening")


    #time_list=[1am,2am,3am,4am,5am,6am,am,2am,2am,2am,2am,2am,2am,2am,]