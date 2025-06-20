# userinput= list(map(int,input("numbers:").split()))
# def filter_even(numbers):
#     return list(filter(lambda x: x % 2 == 0, numbers))

# print(filter_even([1, 2, 3, 4, 5, 6]))

# def add(a, b):
#      return a + b
# def subtract(a, b):
#      return a - b
# def multiply(a, b):
#      return a * b
# def divide(a, b): 
#      return a / b

# a, b = 10, 5
# print("Add:", add(2, 2))
# print("Subtract:", subtract(a, b))
# print("Multiply:", multiply(a, b))
# print("Divide:", divide(a, b))

# def check_number():
#      n=int(input("enter the no"))
#      if n%2==0:
#           print("number is even")
#      else:
#           print("not")
# check_number()

# with open("sample.txt", "w") as f:
#     f.write("Hello Python!\n")

# with open("sample.txt", "r") as f:
#     print(f.read())

# import re

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return bool(re.match(pattern, email))

# print(validate_email("abc@34gmail.com"))

# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# even_squared = list(filter(lambda x: x % 2 == 0, squared))
# print(even_squared)

# import math

# print(math.sqrt(16))
# print(math.log(100))
# print(math.pow(2, 3))


# value = input("Enter a value: ")
# print(int(value), type(int(value)))
# print(float(value), type(float(value)))
# print(str(value), type(str(value)))
# s = "Hello World"
# print(s.upper())

# print(s.lower())

# print(s.replace("World", "Python"))

# print(s.count("l"))


# a=int(input("enter a 1st number:"))
# b=int(input("enter a 2nd number:"))
# print(a+b)

# for i in range(1,101):
#     print(i)


# a=int(input("enter the number: "))
# if a%2==0:
#     print("number is even ")
# else:
#     print("odd")

# b=int(input("enter our age:"))
# if b>18:
#     print("can vote")
# elif b==12:
#      print("minor")
# else:
#     print("cannot vote")

def fun(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
fun(23)

def add(x, y):
    result = x + y
    return result

sum_result = add(5, 3)
print(sum_result) 


a=7
b=3
print(a+b)
add=a+b
print(add)