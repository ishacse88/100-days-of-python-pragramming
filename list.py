marks=[1,3,5,"isha",True,"isha"]
print(marks)
print(marks[3])
print(type(marks))
print(marks[-3]) 
print(marks[:])
print(marks[0:5:2])
# 5
if 15 in marks:
    print("yes there in list")
else:
    print("no")

if "isha" in marks:
   print("yes there")
else:
    print("no")
if "sha" in "isha":
  print("yes")

lst = [i for i in range(5)]
print(lst)      
lst1 = [i*i for i in range(5) if i%2==0]
print(lst1)


# function used in lists
marks1= [21,7,99,99]
print(marks1)
# marks1.append(5)
# marks1.sort()
# marks1.sort(reverse=True)
# print(marks1.index(99)) 
# marks1.reverse
# print(marks1.count(99))
# marks1.insert(1,22)
m=[900, 1000,1100]
k=marks+m 
print(k)
# marks1.extend(m)

print(marks1)