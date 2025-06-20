
students = {
    "Anisha": 85,
    "jyoti": 92,
    "harsh": 78,
    "isha": 88
}
print("",students)
highest_student = max(students, key=students.get)
highest_marks = students[highest_student]

print("Student with highest marks:")
print("Name:", highest_student)
print("Marks:", highest_marks)