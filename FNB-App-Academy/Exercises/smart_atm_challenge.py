# Set the initial bank balance
balance = 500

# Ask the user how much they want to withdraw
withdrawal = float(input("Enter the amount you want to withdraw (R): "))

# Check the withdrawal amount
if withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")
else:
    print("Declined. Insufficient funds.")