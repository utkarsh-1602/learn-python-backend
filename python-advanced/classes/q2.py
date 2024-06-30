class Dog:
    def __init__(self, name, age):
        self.name = name  # 'self' refers to the instance attribute 'name'
        self.age = age    # 'self' refers to the instance attribute 'age'

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1  # 'self' allows access to the instance attribute 'age'
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating an instance of Dog
my_dog = Dog("Buddy", 5)

# Accessing methods and attributes using 'self'
my_dog.bark()         # Buddy says woof!
my_dog.birthday()     # Happy Birthday, Buddy! You are now 6 years old.
