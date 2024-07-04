class Example:
    def __init__(self, value):
        self.__internal = value # Private attribute initialization

    def my_fun(self):
        return self.__internal # Method to access the private attribute

inst01 = Example(10)
inst02 = Example(20)

print(inst01.my_fun())
print(inst02.my_fun())

