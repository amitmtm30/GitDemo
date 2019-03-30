"""Dictionary is a data type which store more than one vale in a single variable
Dictionary is not Sequence
works on Mapping not Indexing
Mapping means key value pair"""

car = {'make':'bmw', 'model' : '550i', 'year': '2016'}
cars = {'BMW':{'model':'550i','year' : 2018},'benz':{'model': '350e', 'year' :2019}}
print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(cars.items())