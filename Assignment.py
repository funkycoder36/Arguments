shut = (input("Do you want to shut down the system? "))

if shut == "yes":
    print("Shutting down")
elif shut == "no":
    print("Shutting down canceled")
else:
    print("Sorry, try responding in 'yes' or 'no'")