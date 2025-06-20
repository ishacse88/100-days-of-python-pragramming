
class Student:
    def __init__(self,name,marksEng,marksMaths,marksHindi):
        self.name=name
        self.marksEng=marksEng
        self.marksMaths=marksMaths
        self.marksHindi=marksHindi
    def cal_Avg(self):
       avg=(self.marksEng+self.marksMaths+self.marksHindi)/3
       print(f"average of {self.name} is:", avg)
    
s1=Student("isha",97,99,92)      
print(s1.name,s1.marksEng,s1.marksMaths,s1.marksHindi)
s1.cal_Avg()




class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"hii,{self.name} your average score is:",sum/3)
s1=Student("ishu baby",[99,98,97])
s1.get_avg()


s1.name="ishu"
s1.get_avg()
