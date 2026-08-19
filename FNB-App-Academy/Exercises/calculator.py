# Collect two numbers from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Display heading
print("\n========== CALCULATOR RESULTS ==========")

# Addition
print(f"Addition:         {round(number1 + number2, 2)}")

# Subtraction
print(f"Subtraction:      {round(number1 - number2, 2)}")

# Multiplication
print(f"Multiplication:   {round(number1 * number2, 2)}")

# Check for division by zero
if number2 != 0:
    print(f"Division:         {round(number1 / number2, 2)}")
    print(f"Floor Division:   {round(number1 // number2, 2)}")
    print(f"Modulus:          {round(number1 % number2, 2)}")
else:
    print("Division:         Error - Cannot divide by zero.")
    print("Floor Division:   Error - Cannot divide by zero.")
    print("Modulus:          Error - Cannot divide by zero.")

print("========================================")