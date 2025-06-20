
class Student:
    def __init__(self,phy,math,chem):
        self.chem=chem
        self.phy=phy
        self.math=math
    #     self.percentage=str((self.phy + self.chem + self.math)/3) + "%"

    # def calculate(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
s1=Student(98,97,99)
print(s1.percentage)      

s1.phy=86
print(s1.phy)
print(s1.percentage)



