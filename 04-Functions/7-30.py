def sum_natural(n):
    if n == 1:
       return 1
    else :
        return n + sum_natural(n-1)
    
def main():
    num = 10
    suma = sum_natural(10)
    print(f'For the {num} the sum is {suma}')
if __name__ == "__main__":
    main()