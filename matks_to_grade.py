def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

marks_list = []

print("Enter 5 marks:")
for i in range(5):
    marks = int(input())
    marks_list.append(marks)

for marks in marks_list:
    grade = get_grade(marks)
    print(f"Marks: {marks} -> Grade: {grade}")