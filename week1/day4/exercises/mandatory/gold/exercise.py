class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Authentication failed")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")
        if amount <= 0:
            raise Exception("Deposit must be a positive amount")
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")
        if amount <= 0:
            raise Exception("Withdraw must be a positive amount")
        self.balance -= amount
        print(f"Withdrawn: {amount}, New Balance: {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")
        if amount <= 0:
            raise Exception("Withdraw must be a positive amount")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Withdrawal would bring balance below minimum")
        self.balance -= amount
        print(f"Withdrawn: {amount}, New Balance: {self.balance}")


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(
            isinstance(acc, BankAccount) for acc in account_list
        ):
            raise Exception("account_list must be a list of BankAccount instances")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try limit, defaulting to 2")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== ATM Menu ===")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                print(f"Welcome {username}!")
                self.show_account_menu(account)
                return
            except:
                continue

        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Exiting.")
            exit()
        else:
            print(f"Login failed. Attempts left: {self.try_limit - self.current_tries}")

    def show_account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                try:
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Logging out...")
                account.authenticated = False
                break
            else:
                print("Invalid option")

if __name__ == "__main__":
    acc1 = BankAccount("alice", "alice123")
    acc2 = MinimumBalanceAccount("bob", "bob123", minimum_balance=100)
    atm = ATM([acc1, acc2], try_limit=3)
