class Square:
   def __init__(self, a):
      self.a = a  # Side length of the square

   def area(self):
      return self.a * self.a  # Area of the square

   def perimeter(self):
      return 4 * self.a  # Perimeter of the square

# Create two squares
square1 = Square(4)
square2 = Square(6)

# Print area and perimeter for square1
print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.perimeter()}')

# Print area and perimeter for square2
print('Square with side 6:')
print(f'Area is {square2.area()}, Perimeter is {square2.perimeter()}')
