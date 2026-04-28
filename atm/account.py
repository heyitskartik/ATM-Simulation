balance = 1000  # initial balance

def get_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    if amount > balance:
        return False
    balance -= amount
    return True