
n=int(input("enter the number of student:"))
marks=[]
for i in range(n):
    mark=int(input("enter student marks(0-100):"))
    marks.append(mark)
print("original marks are:",marks)
grade=[]
for mark in marks:
  if mark>=90:
    grade.append("A")
  elif mark>=75 and mark<90:
      grade.append("B")
  elif mark >= 60 and mark< 75:
   grade.append("C")
  elif mark >= 40 and mark< 60:
   grade.append("D")
  else:
    grade.append("F")
print("grades:",grade)


