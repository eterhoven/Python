def add(*args):
    print(sum(args))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        


add(3,5,6)

calculate(2, add=3, multiply=5)

my_car = Car(model="GTR")
print(my_car.make)
