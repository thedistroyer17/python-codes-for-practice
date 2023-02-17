# Python program to display the current date and time.
# importing date tim module
import datetime
#storing date time in now variable 
now = datetime.datetime.now()
# string added 
print("date and time right now :")
# specifictaion of format of time 
print(now.strftime("%d-%m-%Y  %H:%M:%S"))