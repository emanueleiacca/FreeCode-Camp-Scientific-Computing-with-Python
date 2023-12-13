class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
#we define the category
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
#deposit allows depositing funds into th category
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
#withdraw allows to withdraw rhe funds from the category.It also check if there is enough balance and acts accordingly
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance
#iterating method to calculate the current balance
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
#it check if there are enough funds avaible,in that case it perform a withdraw with amount and transfer description
#if the transfer is successfull, it return True, otherwise False
    def check_funds(self, amount):
        return amount <= self.get_balance()
#check if there are enough founds
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = entry["amount"]
            total += amount
            items += f"{description:<23}{amount:7.2f}\n"
        output = title + items + f"Total: {total:.2f}"
        return output
#to visualize the output: using formatted string we rappresent the category, including title, item description and amount and the total balance

def create_spend_chart(categories):
    total_withdrawals = 0
    category_spending = {}
    category_names = []

    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                total -= entry["amount"]
        category_spending[category.name] = total
        total_withdrawals += total
        category_names.append(category.name)
        #iterates over each category and calculates the withdrawalas for each category

    percentage_spent = []
    for category in category_spending.values():
        percentage = (category / total_withdrawals) * 100
        percentage_spent.append(percentage)
#percentage spent for each category
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentage_spent:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"

    return chart
#genereting the spend chart: the percentage are showed with "o", we can see the value on the vertical axis, below each category is showed

