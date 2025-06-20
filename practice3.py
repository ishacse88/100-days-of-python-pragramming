# # Input three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# # Using nested if-else to find the greatest number
# if a > b:
#     if a > c:
#         print("The greatest number is:", a)
#     else:
#         print("The greatest number is:", c)
# else:
#     if b > c:
#         print("The greatest number is:", b)
#     else:
#         print("The greatest number is:", c)
# Fibonacci Series in a simple way
# n = int(input("Enter the number of terms: "))

# a, b = 0, 1  # First two terms

# print("Fibonacci Series:")
# for i in range(n):
#     print(a)
#     a, b = b, a + b  # Update values

# Simple Python program to demonstrate string functions

# Take input from user
text = input("Enter a string: ")

# Display available functions
print("\nChoose a string function:")
print("1. Convert to UPPERCASE")
print("2. Convert to lowercase")
print("3. Convert to Title Case")
print("4. Remove extra spaces")
print("5. Replace a word")
print("6. Find length of a word")

# Take user choice
choice = int(input("\nEnter your choice (1-6): "))

# Apply selected function
if choice == 1:
    print("Uppercase:", text.upper())
elif choice == 2:
    print("Lowercase:", text.lower())
elif choice == 3:
    print("Title Case:", text.title())
elif choice == 4:
    print("Without extra spaces:", text.strip())
elif choice == 5:
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")
    print("Updated string:", text.replace(old_word, new_word))
elif choice == 6:
     print(len(text))
else:
    print("Invalid choice! Please enter a number between 1 and 6.")

