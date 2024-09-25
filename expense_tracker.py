import json
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, description, amount):
        expense = {
            "id": len(self.expenses) + 1,
            "description": description,
            "amount": amount
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f'Expense "{description}" added.')

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nExpenses:")
        for expense in self.expenses:
            print(f'ID: {expense["id"]}, Description: {expense["description"]}, Amount: ${expense["amount"]:.2f}')
        print()

    def update_expense(self, expense_id, description, amount):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                expense['description'] = description
                expense['amount'] = amount
                self.save_expenses()
                print(f'Expense ID {expense_id} updated.')
                return
        print(f'Expense with ID {expense_id} not found.')

    def delete_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense['id'] != expense_id]
        self.save_expenses()
        print(f'Expense ID {expense_id} deleted.')

def main():
    tracker = ExpenseTracker()
    while True:
        print("Options: add/view/update/delete/exit")
        command = input("Enter a command: ").strip().lower()
        if command == 'add':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
        elif command == 'view':
            tracker.view_expenses()
        elif command == 'update':
            expense_id = int(input("Enter expense ID to update: "))
            description = input("Enter new expense description: ")
            amount = float(input("Enter new expense amount: "))
            tracker.update_expense(expense_id, description, amount)
        elif command == 'delete':
            expense_id = int(input("Enter expense ID to delete: "))
            tracker.delete_expense(expense_id)
        elif command == 'exit':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
