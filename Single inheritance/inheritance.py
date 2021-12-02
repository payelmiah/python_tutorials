class Vehical:
    def normal_uses(self):
        print("Hi, i'm a vehical")
class car(Vehical):
    def __init__(self):
        print("i am a car")
        self.wheels=4
        self.roop = True
    def spacific_uses(self):
        self.normal_uses()
        print("spacifice uses for car uses for family")
class motorbike(Vehical):
    def __init__(self):
        print("i am motor bike")
        self.wheels=2
        self.roop=False
    def spacific_uses(self):
        self.normal_uses()
        print("spacific uses for single")

c=car()
c.spacific_uses()

m=motorbike()
m.spacific_uses()

print(isinstance(c,car)) #check c object instead of c
print(issubclass(car,Vehical)) # check car would be subclass of Vehical or not