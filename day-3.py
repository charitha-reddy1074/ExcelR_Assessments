# Function to calculate the grade based on average marks
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        return "Grade: A"
    elif 80 <= average < 90:
        return "Grade: B"
    elif 70 <= average < 80:
        return "Grade: C"
    else:
        return "Grade: Fail"

# Input marks for three subjects
marks = []
for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate and print the grade
grade = calculate_grade(marks)
print(grade)