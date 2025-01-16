def f(prods,fnc):
    return str(list((map(fnc,prods)))).replace(" ","")[1:-1]

prods = ["woda", "ser", "pomidor"]
fnc1 = lambda x: "id:"+x[:2]
print(list(map(fnc1,prods)))
print((f(prods,fnc1)))
