# Create a dictionary of contacts
contacts = {
    "Amara": "0821112222",
    "Sipho": "0833334444",
    "Lerato": "0845556666"
}

# Ask the user for the friend's name
name = input("Enter the name of the friend you want to look up: ")

# Check if the contact exists
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")