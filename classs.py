# name
# color
# cylinder
# module
#  price
class Car:

    print("new car")
    name = ""
    color = ""
    cylinder = 6
    module = 1900
    price = 12.00

    def __init__(self, name, color, cylinder, module, price):
        print("new car")
        self.name = name
        self.color = color
        self.cylinder = cylinder
        self.module = module
        self.price = price
car_1 = Car("mercedes", "black", 6, 1900, 12.000)
print(car_1.name)


