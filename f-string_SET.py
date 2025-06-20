letter="hey my name is {} and i am from{}"
country="india"
name="harry"

print(letter.format(country,name))
print(f"hey my name is {name} and I am from {country}")
price= 49.09999
txt = f"for only {price:.2f} dollars"
print(txt)
print(type(f"{2*30}"))
print(f"hey my name is {{name}} and I am from {{country}}")




def fabonacci(n):
 if(n==0):
      return 0
 elif(n==1):
    return 1
 else:
    return fabonacci(n-1) + fabonacci(n-2)
print(fabonacci(7))

# set
s={2,3,2,"isha",False,"code","code"}
print(s)

info=set()
print(type(info))

for data in s:
   print(data)

s1 = {1,2,5,6}
s2 ={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)   
 
cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3= cities.union(cities2)
cities3=cities.intersection(cities2)
cities3=cities.symmetric_difference(cities2) #unique value among both
cities3=cities.difference(cities2)
print(cities3)
cities.intersection_update(cities2)
print(cities)





