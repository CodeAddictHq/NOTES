#Encapsulation means wrapping data and methods together inside a class and restricting direct access to some parts of the data
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__update_balance(amount)

    def get_balance(self):
        return self.__balance

    # internal method (encapsulated)
    def __update_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

acc = BankAccount(1000)

acc.deposit(500)
print(acc.get_balance())
"""__balance → private data
__update_balance() → private method (cannot be called outside)
Only deposit() is exposed to user
"""