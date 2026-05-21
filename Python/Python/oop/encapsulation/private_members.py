# Private members: attributes/methods not meant for outside access
# Convention: prefix with _ (protected) or __ (private/name-mangled)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private — name-mangled to _BankAccount__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())   # 150

# Direct access raises AttributeError:
# print(account.__balance)

# Still accessible via mangled name (not recommended):
# print(account._BankAccount__balance)
