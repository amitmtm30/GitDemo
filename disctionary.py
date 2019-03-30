"""Dictionary is a data type which store more than one vale in a single variable
Dictionary is not Sequence
works on Mapping not Indexing
Mapping means key value pair"""

cars = {'make':'bmw', 'model' : '550i', 'year': '2016'}
d ={}
print(cars['make'])
model = cars['model']
print(model)
d['one'] = 1
d['two'] = 2
cars['cost'] = 3500000
print(cars)
print(d)
sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)
