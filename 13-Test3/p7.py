def f(arr2D):
    lista = []
    for i in range(len(arr2D[0])):
        sum = 0
        for j in arr2D:
            sum += j[i]
            print("Obrót")
        if sum in lista:
            print(lista)
            return True
        lista.append(sum)
    return False
print(f([[0,1,2],
         [3,2,1]]))
    