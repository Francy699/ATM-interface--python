class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
        self.balance = 0

    def __str__(self):
        return f"{self.type}: ${self.amount}"


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_history(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("Transaction History:")
        for idx, transaction in enumerate(self.transactions, 1):
            print(f"{idx}. {transaction}")


class ATM:
    def __init__(self):
        self.balance = 1000
        self.transaction_history = TransactionHistory()

    def check_balance(self):
        print(f"Your current balance is ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction('Deposit', amount)
            transaction.balance = self.balance
            self.transaction_history.add_transaction(transaction)
            print(f"Deposited ${amount}. Your new balance is ${self.balance}")
        else:
            print("Invalid amount. Please deposit an amount greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            transaction = Transaction('Withdraw', amount)
            transaction.balance = self.balance
            self.transaction_history.add_transaction(transaction)
            print(f"Withdrew ${amount}. Your new balance is ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(f'Transfer to {recipient}', amount)
            transaction.balance = self.balance
            self.transaction_history.add_transaction(transaction)
            print(f"Transferred ${amount} to {recipient}. Your new balance is ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

def main():
    atm = ATM()

    while True:
        print("\n==== ATM Menu ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter option (1/2/3/4/5/6): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            amount = float(input("Enter the amount to transfer: "))
            recipient = input("Enter the recipient's name: ")
            atm.transfer(amount, recipient)
        elif choice == '5':
            atm.transaction_history.display_history()
        elif choice == '6':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
