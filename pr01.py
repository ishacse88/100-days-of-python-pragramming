# Get user input for email and password
email = input("Enter your email: ")
password = input("Enter your password: ")

# Email validation: Must contain '@' and 'gmail'
if "@" in email and "gmail" in email:
    email_valid = True
else:
    email_valid = False
    print("Invalid email! Email must contain '@' and 'gmail'.")

# Password validation
if len(password) > 10 and any(char.isdigit() for char in password) and \
   any(char.isalpha() for char in password) and \
   any(not char.isalnum() for char in password):
    password_valid = True
else:
    password_valid = False
    print("Invalid password! Password must be greater than 10 characters, include a number, a letter, and a special character.")

# Final check
if email_valid and password_valid:
    print("Email and Password are valid!")
else:
    print("Please enter valid email and password.")
