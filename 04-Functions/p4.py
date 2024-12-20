def f(subjects):
    przedmioty = list(subjects.keys())
    oceny = list(subjects.values())
    
    średnia = []
    for n in range (len(przedmioty)):
        sum = 0
        num = len(oceny[n])
        for o in range (len(oceny[n])):
            sum += oceny[n][o]
        średnia.append(sum/num)
    nazwa = max(średnia)
    for s in range (len(średnia)):
        if średnia[s] == nazwa :
            return przedmioty[s]
        




def main():
    subjects = {
        "math" : [2, 4, 5],
        "geo" : [ 3, 4],
        "comp" : [4, 4]
    }
    print(subjects.values())
    print(f(subjects))
    a = "2"
    print(int(a))
if __name__ == "__main__":
    main()
        