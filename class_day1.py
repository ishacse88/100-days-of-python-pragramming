class Student:
    # name="isha"
    def __init__(self,fullname,marks):
        print(self)
        self.name= fullname
        self.marks=marks
        print("info for student...")
    def welcome(self):
        print("welcome", self.name)
        # return self.name
    def get_marks(self):
        return self.marks
    
s1=Student("isha",97.9)
print(s1.name,s1.marks)
s1.welcome()
# print(s1.welcome())
print(s1.get_marks())


 
     