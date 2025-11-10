""" This program defines two classes: Transaction and PersonAccount.
- Transaction class is used to store individual income or expense entries
  with a description and the amount.
- PersonAccount class manages the users personal account by maintaining
  lists of incomes and expenses. It provides the functionality to add
  incomes and expenses, calculate total income, total expense, and
  compute the account balance. """

class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []     # list of Transaction objects

    def add_income(self, description, amount):
        self.incomes.append(Transaction(description, amount))

    def add_expense(self, description, amount):
        self.expenses.append(Transaction(description, amount))

    def total_income(self):
        return sum(income.amount for income in self.incomes)

    def total_expense(self):
        return sum(expense.amount for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Account Details\nFirst Name: {self.firstname}\nLast Name: {self.lastname}\nBalace: {self.account_balance()}")
        
        print("\n--- Incomes ---")
        for income in self.incomes:
            print(f"{income.description} : {income.amount}")

        print("\n--- Expenses ---")
        for expense in self.expenses:
            print(f"{expense.description} : {expense.amount}")

        print("\nTotal Income :", self.total_income())
        print("Total Expense:", self.total_expense())
        print("Balance      :", self.account_balance())


person = PersonAccount("Sai", "Kiran")

person.add_income("Salary", 50000)
person.add_income("Freelancing", 15000)

person.add_expense("Rent", 12000)
person.add_expense("Internet", 1000)

person.account_info()