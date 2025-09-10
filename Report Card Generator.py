print("Welcome to Student Report Card Generator")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

subjects = ["Mathematics","Science","English","Computer","Social Studies"]
marks = []

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks.append(score)

total = sum(marks)
average = total / len(subjects)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"    
elif average >= 60:
    grade = "C"
else:
    grade = "D"

# Print Report Card
print("\n____REPORT CARD____")
print(f"Name: {name} ")
print(f"Roll No: {roll} ")
for subject,score in zip(subjects,marks):
    print(f"{subject}: {score}")
print("--------------------")
print(f"Total Marks: {total} ")
print(f"Average: {average}")
print(f"Grade: {grade}")
print("--------------------")
print("Report Card Generated Successfully!")