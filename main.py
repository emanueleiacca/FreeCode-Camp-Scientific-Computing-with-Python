from budget import Category, create_spend_chart
#we import Category that we defined on budget.py
food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")
# Create category objects

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(10.15, "Groceries")
food_category.withdraw(15.89, "Restaurant and more food")
food_category.transfer(50, clothing_category)

clothing_category.deposit(500, "Initial deposit")
clothing_category.withdraw(25.55, "Clothes")
clothing_category.transfer(75.50, auto_category)

auto_category.deposit(1000, "Initial deposit")
auto_category.withdraw(100.12, "Gasoline")
# Perform deposits and withdrawals

# Print the categories
print(food_category)
print(clothing_category)
print(auto_category)

# Create and print the spend chart
categories = [food_category, clothing_category, auto_category]
spend_chart = create_spend_chart(categories)
print(spend_chart)
