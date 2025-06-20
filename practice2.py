

# if "@" in email and "gmail.com" in email:
#     email_valid = True
# else:
#     email_valid = False
#     print("Invalid email! Email must contain '@' and 'gmail'.")


# if len(password) <= 10:
#     print("Password must be greater than 10 characters.")
# elif password.isalnum():
#     print("Password must include at least one special character.")
# elif password.isalpha():
#     print("Password must include at least one number and one special character.")
# elif password.isdigit():
#     print("Password must include at least one letter and one special character.")
# else:
#     print("Password is valid.")

# if email_valid :
#     print("Email are valid!")
# username=input("enter your username:")
# password = input("Enter your password: ")
# correct_username="isha"
# correct_password="1234"
# if username==correct_username and password==correct_password:
#     print(f"welcome!{username}")
# elif():
#     for attempts in range(3):
#         print("incorrect...try again")
#         password=input("enter the your:")
#         if password==correct_password:
#             print(f"welcome!{username}")
#             break
#         else:
#             print("acess denied")
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# # Define correct username and password
# correct_username = "isha"
# correct_password = "1234"

# # Check if username and password are correct on the first try
# if username == correct_username and password == correct_password:
#     print(f"Welcome, {username}!")
# else:
#     # Allow the user to try 3 times
#     for attempts in range(3):
#         print("Incorrect password. Try again.")
#         password = input("Enter your password: ")
#         if password == correct_password:
#             print(f"Welcome, {username}!")
#             break
#     else:
#         print("Incorrect password entered 3 times. Access denied.")


# Create a Python program that initializes an empty list called student_marks.
#  Ask the user to input 5 student marks and store them in the list.
#  After that, display the list of student marks.

# student_marks=[]
# marks=list(map(int,input("enter 5 student marks").split()))
# student_marks.append(marks)
# print(marks)

# Create a program that stores 7 integers in a list using append(). 
# After the list is populated, display the maximum and minimum numbers in the list.

# Initialize an empty list
numbers = []

# Collect 7 integers from the user
for i in range(7):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)  # Add the number to the list

# Find the maximum and minimum numbers
max_num = max(numbers)
min_num = min(numbers)

# Display the results
print("\nNumbers entered:", numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

