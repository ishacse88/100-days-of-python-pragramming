# x=int("10") + float("5.5")
# print(x)
# y=int(10) + float(5.5)
# print(y)
# a="HeLLlo Wworld"
# print(a.lower())



# Program to handle file not found error

# filename = input("Enter filename: ")

# try:
#     with open(filename, 'r') as file:
#         content = file.read()
#         print("\nFile content:\n")
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found.")
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Error: Invalid input")
# else:
#     print("You entered:", num)

num = int(input("Enter a number: "))

assert num > 0, "Number must be positive"
print("You entered a positive number.")

