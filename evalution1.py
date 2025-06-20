# import random
# secret_number = random.randint(1, 100)
# while True:
#     try:
#         guess = int(input("Enter your guess: "))

#         if guess < secret_number:
#             print("Too low! Try again.")
#         elif guess > secret_number:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You guessed the number {secret_number} correctly!")
#             break  # Exit the loop
#     except ValueError:
#         print("Invalid input! Please enter a valid number.")

# def factorial(n):
#     if n==0 or  n==1:
#         return n
#     else:
#        return n*factorial(n-1)
# print(factorial(5))
# i=1
# while(i<=100):
#  i+=1
#  if i%2==0:
#   print(i)
 
# number=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{number}*{i} = {number*i}")


# user=list(map(int,input("enter the numbers:").split()))
# count=0
# for i in user:
#     count+=i
# print("sum of numbers:",count)

# user=input("enter the sentence:").split()
# words_count=len(user)
# print("total  words ", words_count)

# number=list(map(int,input("enter the number:").split()))
# number.sort()
# print("sorted lists:",number)

# def add_numbers(n,m):
#     return n+m
# print(add_numbers(2,3))

def reserved():
    userinput=input("enter the letter to be reversed:")
    for i in userinput(n-1,0):
        print(userinput)

    