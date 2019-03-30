class Car(object):
    def __init__(self, make, model='550i'):
        self.make = make
        self.model = model
    def inf0(self):
        print("Make of the car :" +self.make)
        print("Model of the car :" +self.model)

c1 = Car('BMW')
print(c1.make)
print(c1.model)
c1.inf0()
c2 = Car('BENZ')
print(c2.make)
print(c2.model)
c2.inf0()
