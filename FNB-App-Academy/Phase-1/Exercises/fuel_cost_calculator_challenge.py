# Ask the user for the distance they want to drive
kilometers = float(input("Enter the number of kilometers you want to drive: "))

# Ask for the current petrol price per liter
petrol_price = float(input("Enter the current petrol price per liter (R): "))

# Calculate the liters of fuel needed
liters_needed = kilometers / 10

# Calculate the total fuel cost
total_cost = liters_needed * petrol_price

# Display the results
print("\n------ Fuel Cost Summary ------")
print(f"Distance: {kilometers} km")
print(f"Fuel Needed: {round(liters_needed, 2)} liters")
print(f"Petrol Price: R{round(petrol_price, 2)} per liter")
print(f"Total Fuel Cost: R{round(total_cost, 2)}")