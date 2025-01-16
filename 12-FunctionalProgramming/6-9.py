weather_in_cities = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

check_weather = list(filter(lambda weather : weather_in_cities[weather]>0, weather_in_cities))
print(f'Cities with positive temperature:{check_weather}')