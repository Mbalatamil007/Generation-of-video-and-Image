students = {}

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"

count = int(input("How many students? "))

for _ in range(count):
    name = input("\nEnter student name: ")
    marks = []

    for subject in range(1, 4):
        mark = float(input(f"Enter mark for subject {subject}: "))
        marks.append(mark)

    students[name] = marks

print("\nStudent Results")
for name, marks in students.items():
    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    print(f"{name}: Marks = {marks}, Average = {average:.2f}, Grade = {grade}")