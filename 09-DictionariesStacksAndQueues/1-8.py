# Price list of items in the clothing store
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# 1. Print list of products and prices before discount
print("Products and their prices before the discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

# 2. Calculate and print the total value of products before discount
total_before_discount = sum(price_list.values())
print(f"\nTotal value of products before the discount: ${total_before_discount:.2f}")

# 3. Apply 10% discount and update prices (round to 2 decimal places)
for product in price_list:
    price_list[product] = round(price_list[product] * 0.90, 2)

# 4. Print list of products and prices after the discount
print("\nProducts and their prices after the 10% discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

# 5. Calculate and print the total value of products after the discount
total_after_discount = sum(price_list.values())
print(f"\nTotal value of products after the discount: ${total_after_discount:.2f}")
