<<<<<<< HEAD
interesting_cities = [
    'Edmonton',
    'Paris',
    'Munich',
    'Berlin',
    'Amsterdam',
    'Prague',
]

germany_cities = ("Munich", "Berlin")
interesting_cities.remove('Edmonton')
new_city = input("Enter a city that interests you: ")
interesting_cities.append(new_city)
interesting_cities.sort()
print (interesting_cities)

for city in interesting_cities:
    if city not in germany_cities:
        print(f"{city} is an interesting city that we can visit")




=======
interesting_cities = [
    'Edmonton',
    'Paris',
    'Munich',
    'Berlin',
    'Amsterdam',
    'Prague',
]

germany_cities = ("Munich", "Berlin")
interesting_cities.remove('Edmonton')
new_city = input("Enter a city that interests you: ")
interesting_cities.append(new_city)
interesting_cities.sort()
print (interesting_cities)

for city in interesting_cities:
    if city not in germany_cities:
        print(f"{city} is an interesting city that we can visit")




>>>>>>> ae1b7d8f4bdc9eed5a1a8dedcf3c696f96f2ec56
