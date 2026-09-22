# Student Grade Calculator
# Week 2 Python Internship Project


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def get_message(grade):
    if grade == "A":
        return "Excellent work! Keep shining!"
    elif grade == "B":
        return "Very Good! Keep it up!"
    elif grade == "C":
        return "Good effort! Keep improving!"
    elif grade == "D":
        return "You can do better! Keep practicing!"
    else:
        return "Don't give up! Keep learning and try again!"


print("===================================")
print("       STUDENT GRADE CALCULATOR")
print("===================================")

student_name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

    except ValueError:
        print("Invalid input! Please enter a number.")


grade = calculate_grade(marks)
message = get_message(grade)

print("\nRESULT FOR", student_name.upper() + ":")
print("Marks:", str(marks) + "/100")
print("Grade:", grade)
print("Message:", message)