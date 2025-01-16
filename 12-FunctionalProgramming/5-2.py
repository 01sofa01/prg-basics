from functools import reduce
numbers = [2,4,6,3,7,5]

even_numbers = filter(lambda x : x %2 == 0, numbers)
if even_numbers :
   sum_of_even_numbers = reduce(lambda x,y : x+y, even_numbers)
print(f'The sum of the even numbers is {sum_of_even_numbers}')