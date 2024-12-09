def f(arr):
    same = None
    if arr[0] == arr[1]:
        same = arr[0]
    else :
        if  arr[0] == arr[2]:
            return arr[1]
        else :
            return arr[0]

    for n in range (2 ,len(arr)):
        if same != arr[n]:
            return arr[n] 
def main():
   card = [7 for x in range(5)]
   card[2] = 5
   print(card)
   print(f(card))

if __name__ == "__main__":
    main()

