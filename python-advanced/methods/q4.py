class Car:
    def __init__(self, vin):
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin) 
        print(_car)
        # cls(vin) is calling the class constructor to create a new instance of the Car class
        # cls(vin) is equivalent to Car(vin).
        # This calls the __init__ method of the Car class, passing vin as the argument
        _car.brand = brand
        print(_car.__class__)
        return _car 
    
car1 = Car('audi')
car2 = Car.including_brand('lamborghini', 'Newbrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)