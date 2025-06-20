    
# num = 20
num=int(input("enter the number:"))
if(num<0):
    print("number is neg")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is btwn 11-20")
    else:
        print("number is greater than 20")
else:
        print("out of bound")
    

import time
timestamp =time.strftime('%H:%M:%S')
print(timestamp)


# match case
u = int(input("enter the number for u:"))
match u:
     case 0:
          print("u is zero")
     case 4:
          print("number is 4")
     
     case _ if u==90:
          print("number is 90 ")
     case _ if u!=80:
          print("number is not equall to 80")
     case _ if u!=40:
          print("number is not equall to 40")
     case _:
           print(u) 
#  for loop    
name="isha"
for char in name:
     print(char)      
     if(char=="s"):
      print("special charchaters now")

      colours=["red", "blue", "green","yellow"]
      for c in colours:
       print(c)
       for i in c:
           print(i)
#  range function 
for char in range(10):
    print(char+2)         
for v in range(12,16):
    print(v)
    for n in range(3,10,2):
        print(n)
# while loop
# i=5
# while(i>0):
#   print(i)
# i=i + 1


# while loop with else
count=int(input("enter the number:"))
while(count>0):
 print(count)
 count= count - 1
else:
    print("i am else")
# break and continue statement

for i in range(11):
#   print("5 X " ,i,"=" ,(5*i))
  if(i==5):
     continue
#   print("5 X " ,i,"=" ,(5*i))
  
