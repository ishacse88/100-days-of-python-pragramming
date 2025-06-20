
class A:
    varA="welcome to class A"
class B:
    varB=("b")
class C(A,B):
    varc=("c")
c1=C()
print(c1.varc)
print(c1.varA)
print(c1.varB)

# super method--is used to access methods of the parent class

class Car:
    def __init__(self,type):
        self.type=type

    def start(self):
        print("car started..")

    def stop(self):
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
       
        super().__init__(type)
        self.name=name
        super().start()

car1=ToyotaCar("fortuner","petrol")
print(car1.type)