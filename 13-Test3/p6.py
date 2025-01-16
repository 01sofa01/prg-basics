def f(vname):
    if not (vname[0].isalpha() or vname[0] == "_"):
        return False
    
    if not len(vname)<=5:
        return False

    for char in range(len(vname)):
        if vname[char].isnumeric() or vname[char].isalpha() or vname[char] == "_":
            continue
        else :
            return False
    return True
print(f("abcde"))
print(f("ab?de"))
