class TankError(Exception):
    pass

class Tank:

    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, amount):

        if amount > 0:
            if amount < self.capacity:
                self.__level = amount
            else:
                raise TankError("Too much liquid in the tank")
        elif amount < 0:
            raise TankError("Not possible to set negative liquid level")
        
    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None

    
# our_tank object has a capacity of 20 units
our_tank = Tank(20)

# our_tank's current liquid level is set to 10 units
our_tank.level = 10

# adding additional 3 units (setting liquid level to 13)
our_tank.level += 3

# let's try to set the current level to 21 units
# this should be rejected as the tank's capacity is 20 units
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)


# In Python, when you use the += operator on an attribute that has a setter defined (like our_tank.level += 3), Python internally calls the setter method (level.setter) to update the attribute. This is part of Python's mechanism to maintain encapsulation and enforce property rules when modifying attributes.

# let's try to set the liquid level to a negative amount
# this should be rejected as it is senseless
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

print('Current liquid level:', our_tank.level)

del our_tank.level

print('Current liquid level:', our_tank.level)
