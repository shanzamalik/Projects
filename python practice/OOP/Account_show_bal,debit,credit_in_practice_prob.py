class Account:
  
    def __init__(self, bal, acnt):
        print("constructor")
        self.balance=bal
        self.account_no=acnt

    
    def show_bal(self):
       
        print("Balance detail:",self.getbalance())
    
    def show_debit(self,debit_money):
        self.balance-=debit_money
        print("Rs",debit_money," was debited from ur account ")
        print("Remaining balance:",self.getbalance())

    def show_credit(self,credit):
        self.balance+=credit
        print("Rs",credit," was credited to ur account ")
        print("New balance:",self.getbalance())

    def getbalance(self):
        return self.balance

acc1=Account(10000,12345)


acc1.show_debit(1000)
acc1.show_credit(500)
acc1.show_credit(40000)
acc1.show_bal()

        