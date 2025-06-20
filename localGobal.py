x=4           # global variable
print(x)

def hello():
    x=5
    print(x)
    print("the local x is:",x)
    print("hello")
print("the global x is:",x)
hello()
print("the global x is " , x)