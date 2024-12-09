def f(macierz):
    sum_row = []
    sum_col = []
    for row in range ((len(macierz))):
        sum = 0
        for element in range (len(macierz[0])):
            sum += element 
        sum_row.append(sum)
    for col in range (len(macierz[0])):
        sum= 0
        for element in range (len(macierz)):
            sum += element
        sum_col.append(sum)
    check = True
    for element in range (len(sum_col)):
        if sum_col[element] != sum_row[element]:
            check = False
            break
    return check 
def main():
   card = [[3,7, 2], [4, 2, 5], [5,2,1]]
   print(f(card))

if __name__ == "__main__":
    main()
        
