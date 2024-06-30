class Duck:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def walk(self):
        pass

    def quack(self):
        return print("Quack")


myduck = Duck(20, "donald")

print(Duck.__class__) # the Duck class is of the 'type' type;
print(myduck.__class__) # the myduck object is an instance type built on the basis of the Duck class, and residing in the __main__ scope;
print(myduck.name.__class__) # the myduck.name is an attribute of the 'str' type
print(myduck.age.__class__)# the myduck.age is an attribute of the 'int' type
print(myduck.quack.__class__) # myduck.quack is an attribute of the 'method' type
