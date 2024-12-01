def in_range (x,y,z):
    if z >= x and z <= y :
        return True
    else:
        return False 
def main():
    n=7
    x=2
    y=15
    zegar = in_range(x, y, n)
    print(zegar)
    print(f'A number: {n}')
    if zegar== True :
        zegar = 'yes'
    else:
        zegar = 'no'
    print(f'Number {n} in the range  ({x}, {y}): {zegar} ')
if __name__ == "__main__":
    main()