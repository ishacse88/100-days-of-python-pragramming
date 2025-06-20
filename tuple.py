# tuple cannot be change
tup=(1,5,6,"green")
print(type(tup), tup)
print(tup[3])
print(tup[-3])

if "green" in tup:
    print("yes present in tuple")
else:
    print("no")
print(tup[1:5])

countries = ("india", "america","spain","italy")
temp = list(countries)
temp.append("germany")
temp.pop(2)              #remove spain
temp[2]="finland"          #add finland at index 2
countries = tuple(temp)
print(countries)

state=("jharkhand" , "bihar", "uttar pradesh","punjab")
state1= ("adhar pradesh","himachal pradesh")
allState = state + state1
print(allState)


tuple1=(0,1,2,3,3,2,1)
print(tuple1.count(3))
print(tuple1.index(3))
print(tuple1.index(2,4,6))
res=len(tuple1)
print("length of tuple:", res)





