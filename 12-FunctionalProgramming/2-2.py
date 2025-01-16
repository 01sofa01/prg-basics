#Unsorted list of names
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
# Sort the list using sorted() with a lambda function as the key
sorted_names = sorted(names, key=lambda x: len(x))

# Display the results
print("Unsorted list:")
print(names)

print("\nSorted list by length:")
for name in sorted_names:
    print(name)
