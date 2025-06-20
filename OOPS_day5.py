# multi level inheritence
class Car:
    def start(self):
        print("car started")
    def stop(self):
            print("car stopped")

class ToyotaCar(Car):
     def __init__(self,brand):
          self.brand=brand
          
class Fortuner(ToyotaCar):
     def __init__(self,type):
          self.type=type

car1=Fortuner("diesel")
car1.start()
print(car1.type)

# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")
# print(car1.name)
# print(car1.start())