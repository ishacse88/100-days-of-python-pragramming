# Basic Types:
# Int: Whole nums (1, 2, 3).
# Float: Decimals (3.14, 2.5).
# Complex: Real+Imag (1 + 2j).
# Bool: True/False.
# Str: Text ("hello").

print('Kolkata')       # single quotes
print("Kolkata")       # double quotes
print('''Kolkata''')   # triple single quotes
print("""Kolkata""") 

a="isha"
d=None
print("the data type of a", type(a))
print("the data type of d is" ,type(d))

f=complex(8*8)
print("datatype:", type(f))
f=int(8*8)
print("datatype:", type(f))

# Container Types:
# List: Ordered items.
# [1, 2, 3]
# Tuple: Ordered, immutable.
# (1, 2, 3)
# Set: Unordered, unique.
# {1, 2, 3}
# Dict: Key-value pairs.
# {'k1': 'v1', 'k2': 'v2'}

list1= [8,2.9,["hello"],[-8,7]]
print(list1)
tuple1=(("xyz","abc"),("str","bye"))
print(tuple1)
dict1={"name":"bebo","age":"21","course":"cse"}
print(dict1)
dict2={   "name":"isha" , "canvote":True , "year":2024}
print(dict2)
