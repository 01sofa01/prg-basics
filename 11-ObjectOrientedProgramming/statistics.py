class Statistics():
    def __init__(self,val: list):
        self.set = val
        
    def add(self):
        number = int(input("Enter number:"))
        self.set.append(number)
        print(f'The number {number} has been added to set')
    
    def display(self):
         # Join numbers in the list with spaces and print them
        print((str(self.set)).replace(",","")) 
        self.max()
        self.min()
        self.mediana()
        self.arithmetic_mean()
    def max(self):
        the_greatest_number = max(self.set)
        print(f"The greatest number is {the_greatest_number}")
    
    
    def min(self):
        the_smallest_number = min(self.set)
        print(f"The smallest number is {the_smallest_number}")


    def arithmetic_mean(self):
        sum = 0
        for number in self.set:
            sum += number
            
        arithmetic_mean = sum / len(self.set)
        print(f"The arithmetic mean of numbers in array is {arithmetic_mean}")

    def mediana(self): 
       lista = self.set.copy()
       lista.sort()
       środek = round((len(list((lista)))+1)/2)
       print(f"Mediana is {lista[środek]}") 
    
set = Statistics([1,2,8])
set.add()
set.display()
set.display()

    
            
