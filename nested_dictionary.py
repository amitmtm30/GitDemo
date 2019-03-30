"""Nested Dictionary is a data type which store the another dictionary on a single key
d = {'k1' : {'nestk1': 'newvalue1', 'nestk2' : 'newvalue2'}}
d['k1']['nestk1']
"""

cars = {'BMW':{'model' : '550i', 'year': 2016},'benz':{'model' : 'E350', 'year': 2018}}
bmw_model = cars['BMW']['model']
print(bmw_model)
print(cars['benz']['year'])



