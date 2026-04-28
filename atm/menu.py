from atm.account import get_balance, deposit, withdraw
from atm.transactions import add_transaction, get_statement

def display_menu():
    print("\n====== ATM MENU ======")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Statement")
    print("5. Exit")

def handle_choice(choice):
    if choice == "1":
        print(f"Current Balance: ₹{get_balance()}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
        add_transaction("Deposited", amount)
        print("Amount deposited successfully.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if withdraw(amount):
            add_transaction("Withdrawn", amount)
            print("Please collect your cash.")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("\n--- Transaction Statement ---")
        statement = get_statement()
        if not statement:
            print("No transactions yet.")
        else:
            for t in statement:
                print(t)

    elif choice == "5":
        print("Thank you for using ATM!")
        return False

    else:
        print("Invalid choice!")

    return True