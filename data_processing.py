import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(city['city'])
print("All the cities in", my_country, ":")
print(temps)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
temperature = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temperature.append(float(city['temperature']))
print(sum(temperature)/len(temperature))
print()

# Print the max temperature for all the cities in Italy
# Write code for me
temperature = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temperature.append(float(city['temperature']))
print(max(temperature))
print()

# Let's write a function to filter out only items that meet the condition
def filter(condition, dict_list):
    filtered = []
    for i in dict_list:
        if condition(i):
            filtered.append(i)
    return filtered
x = filter(lambda x: float(x["latitude"]) <= 50.0 and x["country"] == 'Italy', cities)
for i in x:
    print(i)


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    pass

# Let's write code to
# - print the average temperature for all the cities in Italy
temperature = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temperature.append(float(city['temperature']))
print(sum(temperature)/len(temperature))
print()

# - print the average temperature for all the cities in Sweden
temperature = []
my_country = 'Sweden'
for city in cities:
    if city['country'] == my_country:
        temperature.append(float(city['temperature']))
print(sum(temperature)/len(temperature))
print()

# - print the min temperature for all the cities in Italy
temperature = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temperature.append(float(city['temperature']))
print(min(temperature))
print()

# - print the max temperature for all the cities in Sweden
temperature = []
my_country = 'Sweden'
for city in cities:
    if city['country'] == my_country:
        temperature.append(float(city['temperature']))
print(max(temperature))
print()
