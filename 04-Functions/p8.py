def f(expression):
    podzielone = expression.split()
    lista = []
    while podzielone != []:
        if podzielone[0] == "+":
            lista.append(lista.pop(0) + lista.pop(0) )
            podzielone.pop(0)
        elif podzielone[0]== "-":
            lista.append(lista.pop(0) - lista.pop(0))
            podzielone.pop(0)
        else:
            lista.append(int(podzielone.pop(0)))
    return lista[0]
def f2(expression):
    podzielone = expression.split()
    lista = []
    for n in podzielone:
        if n == "+":
            lista.append(lista.pop(0) + lista.pop(0))
        elif n == "-":
            lista.append(lista.pop(0)-lista.pop(0))
        else:
            lista.append(int(n))
    return lista[0]




def main():

    expression = "11 7 + 15 - 4 +"
    print(f(expression))
    print(f2(expression))
if __name__ == "__main__":
    main()
        