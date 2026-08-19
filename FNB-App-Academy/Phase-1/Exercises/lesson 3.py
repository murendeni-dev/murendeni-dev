# Adding two numbers

num1 = (input("Enter the first number: "))
num2 = (input("Enter the second number: "))

# "Hello" +" "World" = "Hello World"
# "5" + "10" = "510"
print(num1 + num2)
print(int(num1) + int(num2))
# Core Data types
# str : String/ Text "hello"
# int : Integer/ whole number 5
# float : Floating point 5.5
# bool : Boolean True/False

# Calculating the bill
bill = float(input("Enter the bill amount:R "))
tip = 0.15 #Written in decimal

val_tip = bill * tip
total_cost = bill + val_tip

print(f"Here is the tip: {val_tip}")
print(f"Here is the tip: {round(val_tip, 2)}rounded")

print(f"Here is the total cost: {round(total_cost)}")
print(f"Here is the total cost: {round(total_cost, 2)} rounded")