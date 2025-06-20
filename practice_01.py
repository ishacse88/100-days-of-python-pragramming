
# user input for addition
userInput=int(input("enter your number for addition:"))
userInput2=int(input("enter your other number for addition:"))
sum =  userInput + userInput2
print("sum of these 2 number is:",sum)

# if elif for printing even numbers btwn 1-10
for num in range(11):
    
    if(num%2==0):
        print("even numbers", num)
    elif():
        print("i am done")

#  print multiplication table using for and while loop (f-string for print statement)
a=int(input("enter number for multiplication"))
for number in range(1,11):
    print(f"{int(a)} X {number} = {a*number}")

# write a program using function 
# recursion based program 
#Create a function to calculate the factorial of a number
def factorial(n):
    #  num= int(input("enter the number for factorial:"))
    if(n==0 or n==1):
      return 0
    elif():
         return n*factorial(n-1)
factorial(5)
# Write a recursive function to reverse a string.
# def reverse_string(word):
#    if (len(word)==1):
#        return word
#    elif():
#        return reverse_string(word[1:])+ word[0]
# input_String = input("enter a string:")

# reversed_string = reverse_string(input_String)
# print("reversed string is:" , reversed_string)


def reverse_string(word):

    if len(word) <= 1:
        
      return reverse_string(word[1:]) + word[0]


input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


# function
def listOfNumbers(numbers):
    evenNum=0
    for num in numbers: 
      if(num%2==0):
         evenNum += num
    return evenNum
input_list=(map(int,input("enter numbers separated by spaces:").split()))
results=listOfNumbers(input_list)    
print("the sum of even numbers is:", results)     

# tuple based questions

tup=(1,5,6,7)
count=0
for num in tup:
    count += num
print("occurences:")
   


