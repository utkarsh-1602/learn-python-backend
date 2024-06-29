# creating a class in python with __init__ and self 

class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def bark(self):
        return f"{self.name} says bhau bhau!"
    

my_dog_instance = Dog("Tommy", 5)
print(my_dog_instance.name)
print(my_dog_instance.age)
print(my_dog_instance.bark())
