# public class example 
class Account:
    def __init__(self, acc_no,acc_psswrd):
        self.acc_no=acc_no
        self.acc_psswrd=acc_psswrd
acc1=Account("123457","abcde")
print(acc1.acc_psswrd)
print(acc1.acc_no)        

# pivate class example
class Bankaccount:
    def __init__(self, acc_No,acc_pss):
          self.acc_No=acc_No
          self.__acc_pss=acc_pss   
    def reset_pss(self):
         print(self.__acc_pss)
acc1=Bankaccount("1234","asdf")
print(acc1.acc_No)
print(acc1.__acc_pss)
print(acc1.reset_pss())
# getting error because that attribute is private inside the class
# and we are accessing this outside the class
# but in reset_pss it is working bcoz it is inside same class



# in python we conceptually implement pivate $public(?attributes nd method)
 