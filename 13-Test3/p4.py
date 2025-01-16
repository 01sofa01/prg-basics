def f(fnc, res):
    
    filtered = list(filter(fnc, res))                   #for item in res if item>50 list.append(item)
    

    difference = max(filtered) - min(filtered)
    return difference


res = [95,90,20,50,70]
fnc1 = lambda x: x>50
fnc2 = lambda x: x>30 and x<90

print(f(fnc1,res))
print(f(fnc2,res))

