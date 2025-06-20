
# polymorphism-when the same operator is alalowed to have different meaning according to the context
# (operators $ dunder fucntion)

class Complex:
    def __init__(self,real,img):
      self.real=real
      self.img=img

    def showNumber(self):
       print(self.real,"i +",self.img,"j")

    def add(self,num2):
       newReal = self.real +num2.real
       newImg = self.img + num2.img
       return Complex(newReal,newImg)
    def __str__(self):
        return f"{self.real}i + {self.img}j"
    
num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
print(num3)
