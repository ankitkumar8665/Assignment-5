# Create dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74
}

# Ask user to enter student name
name = input("Enter the student's name: ")

# Check if student exists in dictionary
if name in student_marks:
    print(f"{name}'s marks:", student_marks[name])
else:
    print("Student not found.")