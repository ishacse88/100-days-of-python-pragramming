
marks=[87,33,99,11,44]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

marks[1]="isha"
print(marks)
print(marks[:3])
print(marks[1:])
print(marks[-3:-1])

# list method
marks.append(100)
marks.sort()
marks.sort(reverse=True)
marks.reverse()

marks.insert(3,89)
print(marks.remove(44))
print(marks.pop(1))
print(marks)

