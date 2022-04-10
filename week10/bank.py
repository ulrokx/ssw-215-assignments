# Richard Kirk - SSW-215 - Scrooge McDuck's Bank
# I pledge I have abided by the Stevens Honor System - RK
class Account:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self._withdraw_count = 0
        self._deposit_count = 0
        self._penalty_count = 0
    def _getMaxWithdraw(self):
        return self.balance * .1
    def withdraw(self, amount, *, override = False):
        if amount > self._getMaxWithdraw():
            if override:
                self.balance -= amount
                return
            self._penalty_count += 1 # add 1 to penalty count
            raise ValueError("You have exceeded your withdraw limit")
        else:
            self.balance -= amount
            self._withdraw_count += 1
    def deposit(self, amount):
        self.balance += amount # add amount to balance
        self._deposit_count += 1
    def getBalance(self):
        return self.balance # return balance
    def getMaxWithdraw(self):
        return self._getMaxWithdraw()
    def __str__(self) -> str:
        return f"{'-' * 20}\nAccount: {self.name}, Balance: {self.balance}, Account Number: {self.account_number} \n Withdraw Count: {self._withdraw_count}, Deposit Count: {self._deposit_count}, Penalty Count: {self._penalty_count}\n{'-' * 20}\n"
    
class ScroogeBank:
    def __init__(self):
        self.scrooge_account_number = 1000001 # account number of scrooge
        self.accounts = [Account("Scrooge", 1000000, self.scrooge_account_number)] # list of accounts
        self.transactions = 0 # number of transactions
    def withdraw(self, amount, * , account_number = 0, name = ""):
        self.transactions += 1
        for a in self.accounts:
            if a.account_number == account_number or a.name == name: # if account_number or name is found
                try: 
                    a.withdraw(amount) # try to withdraw amount from account
                except ValueError:
                    self.transfer(a.account_number, self.scrooge_account_number, 5) # pay penalty
                    return 
                self.scroogeRule(amount, account_number=a.account_number) # do scrooge rule on withdraw
                return
        raise ValueError(f"Account number {account_number} not found")
    def scroogeRule(self, amount, *, account_number = 0, name = ""): # transfer amount to all accounts except the one that withdrew
        for a in self.accounts:
            if a.account_number != account_number and a.name != name and a.account_number != self.scrooge_account_number:
                try:
                    self.transfer(self.scrooge_account_number, a.account_number, amount)
                except ValueError:
                    raise ValueError("Scrooge is out of money!")
    def transfer(self, from_account_number, to_account_number, amount): # transfer amount from one account to another
        for a in self.accounts:
            if a.account_number == from_account_number:
                try: 
                    a.withdraw(amount, override=True) # withdraw amount from from_account_number
                except ValueError:
                    raise ValueError("Insufficient funds")
                for b in self.accounts:
                    if b.account_number == to_account_number:
                        b.deposit(amount)
                        return
                a.deposit(amount) # return amount to from_account_number if to_account_number not found
                raise ValueError(f"Account number {to_account_number} not found")
        raise ValueError(f"Account number {from_account_number} not found")
    def createAccount(self, name, balance, account_number):
        self.accounts.append(Account(name, balance, account_number)) 
    def getStatuses(self):
        print(f"{'-' * 20}\nTransactions: {self.transactions}\n{'-' * 20}")
        for a in self.accounts:
            print(a)
def printAccounts(accounts):
    for a in accounts:
        print(a)
if __name__ == "__main__":
    bank = ScroogeBank()
    bank.createAccount("Huey", 150, 700007)
    bank.createAccount("Dewey", 350, 800008)
    bank.createAccount("Louie", 25, 900009)

    bank.withdraw(2, name="Louie")
    bank.getStatuses()
    bank.withdraw(20, account_number=800008)
    bank.getStatuses()
    bank.withdraw(20, name="Huey")
    bank.getStatuses()
    bank.withdraw(10, name="Louie")
    bank.getStatuses()
    bank.withdraw(20, name="Dewey")
    bank.getStatuses()
    bank.withdraw(30, account_number=700007)
    bank.getStatuses()
    bank.withdraw(40, account_number=900009)
    bank.getStatuses()