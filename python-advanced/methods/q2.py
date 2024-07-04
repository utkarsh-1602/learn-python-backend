class Class1:
    def __init__(self, value):
        self.__internal = value 

    def my_fun(self):
        return self.__internal 

class Class2:
    def __init__(self, value):
        self.value = value

    def my_fun(self):
        return self.value
    

inst01 = Class1(10)
inst02 = Class2(20)

print(inst01.my_fun())
print(inst02.my_fun())

print(inst02.value)
print(inst01.__internal)
