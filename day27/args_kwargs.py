# * args

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1,4,5,6,10)

# ** kwargs

def calculate(**kwargs):
    for k, v in kwargs.items():
        print(kwargs)
        print(k)
        print(v)

calculate(dupa=23, zhopa=1, straka=7)

class Car():
    def __init__(self, **kwargs):
        self.maker = kwargs.get("maker")
        self.model = kwargs.get("model")
        self.year  = kwargs.get("year")
        self.colour = kwargs.get("colour")
        self.seats  = kwargs.get("seats")

my_car = Car(maker="Dodge", model="Durango", year=2014, seats=7)

print(my_car.maker)
print(my_car.model)
