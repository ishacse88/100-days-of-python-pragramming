# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#         self.pi=3.14
#     def area(self):
#        return self.pi*self.radius*self.radius
#     def perimeter(self):
#         return 2*self.pi*self.radius

# c1=Circle(21)
# print("area:",c1.area())
# print("perimeter:",c1.perimeter())

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showDetails(self):
#         return self.role,self.salary,self.department
    
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("ml_engineer","cse",60000)

# eng1=Engineer("isha",22)
# print(eng1.showDetails())

# e1=Employee("softwareEngineer","cse",55000)
# print("details:",e1.showDetails())


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
