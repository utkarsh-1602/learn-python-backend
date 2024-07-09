# Duck typing 

Duck typing in Python is a principle that emphasizes the importance of an object's behavior over its type or class. The idea is that if an object implements certain methods or behaviors, it can be used interchangeably with any other object that also implements those methods, regardless of their explicit relationship in terms of inheritance or type.

```python
class Duck:
    def quack(self):
        print("Quack!")

    def walk(self):
        print("Walks like a duck")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def walk(self):
        print("Walking like a duck!")

def make_it_quack_and_walk(thing):
    thing.quack()
    thing.walk()

duck = Duck()
person = Person()

make_it_quack_and_walk(duck)    # Output: Quack! Walks like a duck
make_it_quack_and_walk(person)  # Output: I'm quacking like a duck! Walking like a duck!

```