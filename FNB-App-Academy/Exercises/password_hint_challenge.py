# Ask the user to enter their secret password
password = input("Enter your secret password: ")

# Remove any leading or trailing spaces
password = password.strip()

# Get the first and last characters of the password
first_letter = password[0]
last_letter = password[-1]

# Display the password hint to the user
print(f"\nPassword Hint: Your password starts with '{first_letter}' and ends with '{last_letter}'.")