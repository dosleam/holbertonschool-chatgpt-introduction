class Checkbook:
    """
    A class representing a checkbook with basic operations to deposit,
    withdraw, and check the balance.
    """

    def __init__(self):
        """
        Initialize a new Checkbook instance with a balance of $0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
        amount (float): The amount of money to deposit. Should be positive.
        """
        if amount <= 0:
            print("The deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Parameters:
        amount (float): The amount of money to withdraw. Should be positive.

        If the amount is greater than the current balance, a message is printed
        indicating insufficient funds.
        """
        if amount <= 0:
            print("The withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        """
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    """
    Main function to interact with the Checkbook class. Prompts the user
    to perform actions such as deposit, withdraw, check balance, or exit.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
