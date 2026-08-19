# List of student dictionaries
students = [
    {"name": "Amara", "maths": 85, "english": 78, "science": 90},
    {"name": "Sipho", "maths": 65, "english": 72, "science": 68},
    {"name": "Lerato", "maths": 45, "english": 58, "science": 52},
    {"name": "Thabo", "maths": 95, "english": 88, "science": 91},
    {"name": "Ayanda", "maths": 35, "english": 42, "science": 39}
]

# List to store processed results
results = []

# Variables for class statistics
total_average = 0
highest_average = 0
lowest_average = 100

# Process each student
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Determine pass/fail
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Save processed result
    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

    # Update class statistics
    total_average += average

    if average > highest_average:
        highest_average = average

    if average < lowest_average:
        lowest_average = average

# Calculate class average
class_average = total_average / len(students)

# Display report
print("\n========== CLASS REPORT ==========")

for result in results:
    print(f"Name    : {result['name']}")
    print(f"Average : {result['average']}")
    print(f"Grade   : {result['grade']}")
    print(f"Status  : {result['status']}")
    print("-------------------------------")

print("\n===== CLASS STATISTICS =====")
print(f"Class Average : {round(class_average, 2)}")
print(f"Highest Average : {round(highest_average, 2)}")
print(f"Lowest Average : {round(lowest_average, 2)}")

# Search loop
while True:
    search = input("\nEnter a student name to search (or type 'exit' to quit): ").strip()

    if search.lower() == "exit":
        print("Program ended.")
        break

    found = False

    for result in results:
        if result["name"].lower() == search.lower():
            print("\nStudent Found")
            print(f"Name    : {result['name']}")
            print(f"Average : {result['average']}")
            print(f"Grade   : {result['grade']}")
            print(f"Status  : {result['status']}")
            found = True
            break

    if not found:
        print("Student not found.")