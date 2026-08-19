# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
favourite_number = input("Enter your favourite number: ")

# Combine first name and surname 
full_name = f"{first_name} {surname}"

# Greeting
print(f"\nWelcome, {full_name}!")

# string manipulation
print(f"Name in uppercase: {full_name.upper()}")
print(f"Name with title case: {full_name.title()}")

# Arithemetic
age_in_months = int(age) * 12
print(f"Your age in months is: {age_in_months}")

# Round favourite number
rounded_number = round(float(favourite_number), 2)
print(f"Your favourite number rounded to 2 decimal places is: {rounded_number}")

# Display data types
print("\nData Types:")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")