
n=int(input("enter the no. of student:"))
marks=[]
for i in range(0,n):
    mark=int(input(f"enter the number{i+1}:"))
    marks.append(mark)
print("marks list:",marks)


passed=0
for mark in marks:
    if mark>=40:
        passed+=1
        
failed = n - passed
print("Passed Students:", passed)
print("Failed Students:", failed)

unique_marks=list(set(marks))

a=sorted(unique_marks)
print(a)
unique_marks.sort()
print("",unique_marks)

if len(unique_marks)>=2:
    second_highest=unique_marks[-2]
    print("second highest:",second_highest)