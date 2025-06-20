name=input("welcome!enter the name:")
age=int(input(f"hello,{name} enter your age:"))
if age>=18 and age.isdigit():
    print("your are an adult")
else:
    print()


hobbies_input = input("Enter your hobbies (separated by commas): ")

# Convert the input string into a list by splitting at commas
hobbies = hobbies_input.split(",")

# Display the list of hobbies
print("Your hobbies are:", hobbies)


