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


data.aggregate("temperature", 
               lambda x : print(min(x),": is the min temperatures for cities in EU that do not have coastlines"), 
               data.filter(lambda y: y["country"] in [k["country"] for k in data().country if k["coastline"]=="yes"],data().city))
data.aggregate("temperature", lambda x : print(max(x),": is the max temperatures for cities in EU that do not have coastlines"),
               data.filter(lambda y: y["country"] in [k["country"] for k in data().country if k["coastline"]=="yes"], data().city))


data.aggregate("latitude", lambda x : print(max(x),"max latitude"), 
               data.filter(lambda y: y["country"] in [k["country"] for k in data().country], data().city))
data.aggregate("latitude", lambda x : print(min(x),"min latitude"), 
               data.filter(lambda y: y["country"] in [k["country"] for k in data().country], data().city))