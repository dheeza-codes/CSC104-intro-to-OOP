from Account import Account
class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)


    def withdraw(self,amount):
        if amount < 2000:
            super().withdraw(amount)

        else:
            print("you can not withdraw above your limit")

savings =  SavingsAccount()
savings.withdraw(2000)