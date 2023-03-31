import Expense

class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if self.sum_expenses(+item) < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages += item

    def __len__(self):
        sum(self.expenses)
        sum(self.overages)

def main():

    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses: ', str(myBudgetList.len()))

if __name__ == "__main__":
    main()
