
students = []

# Collect records for two students
for i in range(2):
    print(f"\n--- Student {i + 1} ---")

    name = input("Enter student name: ").strip()

    marks = []

    # Collect marks for three subjects
    for subject in range(3):
        while True:
            try:
                mark = float(
                    input(f"Enter marks for subject {subject + 1}: ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    # Calculate average
    average = sum(marks) / len(marks)

    # Assign grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    # Store student information
    student = {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    students.append(student)

# Display the final report
print("\n===== STUDENT REPORT =====")

for student in students:
    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Average:", round(student["average"], 2))
    print("Grade:", student["grade"])

print("\nReport completed!")
