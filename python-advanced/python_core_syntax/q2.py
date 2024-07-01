class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight

p1 = Person(30, 40, 50)
p2 = Person(10, 20, 80)

print(p1+p2)