class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self._balance=balance
    def deposit(self,amount):
            self._balance += amount
            print(f"deposited {amount},balance={self._balance}")
    def withdraw(self,amount):
                if amount <= self._balance:
                    self._balance-=amount
                    print(f"Withdrawn {amount},Balance={self._balance}")
                else:
                    print("Insufficient balance") 

class SavingsAccount(BankAccount):
   def add_interest(self):
        interest=self._balance*0.05
        self._balance+=interest
        print(f"interest added:{interest}.Balance={self._balance}")
acc1=BankAccount("Alice",101,1000)
acc2=SavingsAccount("Bob",201,2000)

acc1.deposit(500)
acc1.withdraw(200)
acc2.add_interest()

         
