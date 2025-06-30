
a=int(input("enter first number: "))
b=int(input("enter second number:"))
sum=a+b
sub=a-b
mul=a*b
print(sum, sub, mul, sep="\n")



def is_leap(year):
    if year%4==0:
        return True
    else:
        False
year=int(input(""))
print(is_leap(year))