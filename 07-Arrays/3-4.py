# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a weekday name given the number (1 for Monday, 7 for Sunday)
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with the day meal names separated by commas
def day_meal_plan(meal_plan, day_number):
   meals = meal_plan[day_number - 1]  # Get the meals for the day
   return ', '.join(meals)  # Join the meals with a comma and return the result

# Prints the weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

for i in range(1, 8):  # Loop through the days of the week (1 to 7)
   print(f"{weekday(i)}: {day_meal_plan(meal_plan, i)}")
