# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Initialize totals for each category
food_total = 0
transport_total = 0
utilities_total = 0

# Initialize totals for each week
week_totals = []

# Loop through each week (row)
for row in monthly_expenses:
    food_total += row[0]  # Add food expense for the week
    transport_total += row[1]  # Add transport expense for the week
    utilities_total += row[2]  # Add utilities expense for the week
    week_totals.append(sum(row))  # Calculate total for the week

# Print the results
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)

# Print weekly expenses
for i, week_total in enumerate(week_totals, 1):
    print(f'Week {i}: {week_total}')

print('---------------')

# Print total expenses for the month
total_expenses = food_total + transport_total + utilities_total
print('TOTAL:', total_expenses)
