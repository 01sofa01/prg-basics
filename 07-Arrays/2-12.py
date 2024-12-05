# Categories and expenses
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the index of the maximum expense
max_expense_index = expenses.index(max(expenses))

# Find the corresponding category
most_expensive_category = categories[max_expense_index]
most_expensive_expense = expenses[max_expense_index]

# Print the result
print(f"The most expensive category is {most_expensive_category} with an expense of €{most_expensive_expense}.")
