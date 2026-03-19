class amount:
    def __init__(self,account,balance):
        self.account_no = account
        self.balance = balance
        
    def debit(self,amount):
        if amount > self.balance :
            print("insufficient balance in account !!",)
        else:
            self.balance -= amount
            print(f"RS:{amount} is deducted from acc_no{self.account_no} the available balance is :{self.balance}")
            
    def credit(self,amount):
        self.balance += amount
        print(f"RS:{amount} is credited in your acc_no {self.account_no} the available balance is :{self.balance}")
        
mummy= amount("123456789", 10000)
mummy.credit(200)        
mummy.debit(5000)