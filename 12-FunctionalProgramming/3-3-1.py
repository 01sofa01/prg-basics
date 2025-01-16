fun = lambda x, y: x+y

lista1 = [1,2,3]
lista2 = [6,5,4]

lista3 = list(map(fun, lista1, lista2))
print(lista3)