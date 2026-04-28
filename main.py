from atm.menu import display_menu, handle_choice

def main():
    while True:  # Infinite loop
        display_menu()
        choice = input("Enter your choice: ")
        if not handle_choice(choice):
            break

if __name__ == "__main__":
    main()