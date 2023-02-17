# program to display the version and information of the python installed and the verion info 
import sys
print("instructions:")
choice = int(input("enter 1 to get python info and any other number to exit:"))
if (choice == 1):
    print("python version ~")
    print(sys.version)
    print("version info :")
    print(sys.version_info)
else :
    print("terminated !!!!!!!!!!!!")
