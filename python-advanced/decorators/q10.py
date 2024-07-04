def func_1(class_):
    class_.__mymethod = class_.__getattribute__

    # __getattribute__ is a built-in method in Python that is used to access attributes of an object.

    def new_attribute(self, name):
        if name == 'mileage':
            print('Mileage is good in your bike')
        return class_.__mymethod(self, name)
    
    class_.__getattribute__ = new_attribute
    return class_

@func_1
class Car:
    def __init__(self, mileage):
        self.mileage = mileage

# create an instance and access the attribute
myinst_car = Car(20000)
print(myinst_car.mileage)