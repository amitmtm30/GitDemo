"""This is code for built in method in List"""

More_cars = ["BMW","Alto","Audi","Benz","Tiago"]
length = len(More_cars)
print(length)
More_cars.insert(5, "Beat")
print(More_cars)
x = More_cars.index("Beat")
print(x)
y = More_cars.pop(2)
print(y)
print(More_cars)
More_cars.remove("Benz")
print(More_cars)

print("*#"*30)
print(More_cars)
More_cars.reverse()
print(More_cars)
More_cars.extend("Beat)
print(More_cars)