from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1) # Calls the string method
account1.deposit(1000)
print(account1)
account1.withdraw(1500)
print(account1)
account1.withdraw(1000)
print(account1)

balance = account1.get_balance()
print(balance)

account2 = account1
print(account2)

