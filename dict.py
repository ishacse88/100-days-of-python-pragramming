info = {
    'name':'isha', 'age':19, 'eligible':True
    }

print(info)
print(info['name'])
print(info.get('name'))
print(info.get('eligible'))
print(info.keys())
print(info.values())

# using loop
for key in info.keys():
    print(info[key])
# print in key--value
print(info.items())

for key, value in info.items():
    print(f" the value corresponding to the key {key} is {value}")


stud ={110:45, 120:33, 130:36, 140:49}
stud2={105:25, 106:18}
# stud.update(stud2) 
# stud.clear()
# stud.pop(120)

# stud.popitem()
# print(stud)
del stud[110]
print(stud)
