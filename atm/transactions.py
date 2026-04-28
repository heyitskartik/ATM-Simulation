transactions = []

def add_transaction(type, amount):
    transactions.append(f"{type}: ₹{amount}")

def get_statement():
    return transactions