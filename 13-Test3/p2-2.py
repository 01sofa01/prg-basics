def f(x,y,digit):
    lista = str(list(range(x,y+1)))
    return lista.count(str(digit))

print(f(10,15,1))