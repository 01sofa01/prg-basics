countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Spain", "population": 48000000},
    {"name": "Italy", "population": 58000000},
    {"name": "Portugal", "population": 10000000},
    {"name": "New Zeland", "population": 5000000}
]

for country in countries:
    name = country["name"]
    population = country["population"]
    print(f"Name: {name}, Population: {population}")
