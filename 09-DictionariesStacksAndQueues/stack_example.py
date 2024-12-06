import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     
cards.put('2')
cards.put('3')
cards.put('7')
cards.put('1')
cards.put('9')
cards.put('8')

# Sum of the last two elements
last = cards.get()  # Last element
second_last = cards.get()  # Second-to-last element
sum_last_two = last + second_last
print('Sum of last two elements is:', sum_last_two)

# Calculate the sum of the remaining elements
remaining_sum = 0
while not cards.empty():
    remaining_sum += cards.get()

# Print the sum of the remaining elements
print('Sum of remaining elements is:', remaining_sum)

# Print the total number of stack elements (before removal)
total_elements = 7  # Since we added 7 elements initially
print('Number of stack elements:', total_elements)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

