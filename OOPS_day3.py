
class Account:
    def __init__(self,accountNo,balance=0.0):
        self.balance=balance
        self.accountNo=accountNo
    def credit(self,amount):
        if amount>0:
           self.balance+=amount
           print(f"Rs{amount} is credited to your acc")
        else:
           print("invaild credit amount")

    def debit(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"₹{amount} debited from account {self.accountNo}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid debit amount.")

    def print_balance(self):
        print(f"account : {self.accountNo} balance:Rs {self.balance}")
acc1=Account("1234567890",1000)
acc1.print_balance()
acc1.credit(500)
acc1.debit(300)
acc1.print_balance()