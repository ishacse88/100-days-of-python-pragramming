a=input("enter the number: ")
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11): 
       print(f"{int(a)} X {i} = {int(a)*i}")

# except Exception as e:
#     print(e)
except:
    print("invalid input!")

print("some imp lines of code")
print("end of program")







