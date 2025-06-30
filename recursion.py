
def printNumber(n):
    if(n==1):
        return 
    print(n)
    printNumber(n-1)
printNumber(5)


# Print Numbers from 1 to N
def printnum(n):
    if n==6:
        return 
    print(n)
    printnum(n+1)
printnum(1)


# Print Sum of First N Natural Numbers
def sumNum(n):
    if n==6:
        return 0
    return n+sumNum(n+1)
output=sumNum(1)
print(output)
       
# Calculate Factorial of a Number
def fact(n):
    if n==0 or n==1:
     return 1
    return n*fact(n-1)
print(fact(4))

#  Print a String in Reverse Using Recursion
def reverseString(n):
   if len(n)==0:
      return 
   print(n[-1], end="")
   
   reverseString(n[:-1])
reverseString("h")


def sumnumber(n):
    if n==0:
        return 0
    return n+ sumnumber(n-1)
print(sumnumber(4))