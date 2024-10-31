import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class data:
    def __init__(self):
        self.country = []
        self.city = []

        with open(os.path.join(__location__, 'Countries.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.country.append(dict(r))

        with open(os.path.join(__location__, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.city.append(dict(r))

    def filter(condition, dict_list):
        filtered = []
        for i in dict_list:
            if condition(i):
                filtered.append(i)
        return filtered
    
    def aggregate(aggregation_key, aggregation_function, dict_list):
        keep = []
        for i in dict_list:
            keep.append(float(i[aggregation_key]))
        return aggregation_function(keep)


_min = data.aggregate("temperature", lambda x : min(x), data.filter(lambda y: y["country"] in [k["country"] for k in data().country if k["coastline"]=="yes"], data().city))
_max = data.aggregate("temperature", lambda x : max(x), data.filter(lambda y: y["country"] in [k["country"] for k in data().country if k["coastline"]=="yes"], data().city))
print(_min, _max)













# # Let's write code to
# # - print the average temperature for all the cities in Italy
# avg_temp = aggregate("temperature", lambda x : sum(x)/len(x), filter(lambda y : y["country"] == "Italy", cities) )
# print(avg_temp)
# # - print the average temperature for all the cities in Sweden
# avg_temp = aggregate("temperature", lambda x : sum(x)/len(x), filter(lambda y : y["country"] == "Sweden", cities) )
# print(avg_temp)
# # - print the min temperature for all the cities in Italy
# avg_temp = aggregate("temperature", lambda x : min(x), filter(lambda y : y["country"] == "Italy", cities) )
# print(avg_temp)
# # - print the max temperature for all the cities in Sweden
# avg_temp = aggregate("temperature", lambda x : max(x), filter(lambda y : y["country"] == "Italy", cities) )
# print(avg_temp)
