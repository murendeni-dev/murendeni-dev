# Basic if/else statement script

age = int(input("Please enter your age: "))
section_pass = input("Do you have a VIP ticket? (yes/no): ")

if age >= 18 and section_pass == "yes":
    print(" VIP Access Granted.")
elif age >= 18:
    print("General Access Granted !!!")
else:
    print("Access Denied !!!")

