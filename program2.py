# Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print("date and time right now :")
print(now.strftime("%d-%m-%Y  %H:%M:%S"))