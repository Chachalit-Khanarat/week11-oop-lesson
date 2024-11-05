import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class TableDB:
    def __init__(self):
        self.db = []

    def insert(self, table):
        if self.search(table.table_name):
            print("Table Already Exist")
            return False

        self.db.append(table)

    def search(self, table_name):
        for i in range(len(self.db)):
            if table_name == self.db[i].table_name:
                return self.db[i]
        return False


class Table:
    def __init__(self, table_name = "name", table = []):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered = []
        for i in self.table:
            if condition(i):
                filtered.append(i)
        return filtered
    
    def aggregate(self, aggregation_function, aggregation_key):
        keep = []
        for i in self.table:
            keep.append(float(i[aggregation_key]))
        return aggregation_function(keep)

    def __str__(self):
        return f"table name {self.table_name}\n{self.table}"

db = TableDB()

with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    tb1 = Table(table_name="country",table=[dict(x) for x in rows])

db.insert(tb1)

with open(os.path.join(__location__, 'Cities.csv')) as a:
    rows = csv.DictReader(a)
    tb2 = Table(table_name="city",table=[dict(x) for x in rows])

db.insert(tb2)

tb3= Table(table_name = "havecoastline", 
           table = db.search("city").filter(lambda y : y["country"] in [k["country"] for k in (db.search("country").filter(lambda x : x["coastline"] == "yes"))]))
db.insert(tb3)

print(db.search("havecoastline").aggregate(lambda x : min(x), "temperature"))
print(db.search("havecoastline").aggregate(lambda x : max(x), "temperature"))

for i in db.search("country").table:
    temp = Table(table_name=i["country"], table=db.search("city").filter(lambda x : x["country"] == i["country"]))
    db.insert(temp)
    print(i["country"], end=' : ')
    print(db.search(i["country"]).aggregate(lambda x : max(x) if len(x)>0 else None, "latitude"))