# Classes, instance, Attributes 

- A class is like a "blueprint" for creating objects. or you can say that it is a template for creating objects. 
- If you define a function inside a class, it’s called a method. Methods are used by instances of a class.


```python 

class Dog:
    def __init__(self, name, age):
        self.name = name  # Assigning the name to the instance
        self.age = age    # Assigning the age to the instance

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of Dog
my_dog = Dog("Buddy", 3)

print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark())  # Output: Buddy says woof!

```

- `__init__` : The __init__ method is crucial in object-oriented programming in Python. It is a special method automatically called when an object is created from a class. This method allows us to initialize an object's attributes and perform any necessary setup or initialization tasks. Without __init__, initialization would have to be done manually each time an object is created, leading to potential errors and less maintainable code. So the general idea is, provide all the information your object needs in init. 

- `self` : In Python, the term “self” refers to the custom class used to access the class's members and methods, as well as to create new members. You always pass self as the first argument and you’d typically assign any other keyword arguments to the self.


- **f-string** : the `f` in program indicates an f-string, which is a formatted string literal in Python. It allows you to include expressions inside curly braces {} directly within the string. Here, self.name is evaluated, and its value is included in the string.

- [Refer q1.py](q1.py)
- [Refer q2.py](q2.py)



## Instance variables

- Python allows for variables to be used at the instance level or the class level.
- Those used at the instance level are referred to as **instance variables**.

```python 
class Demo:
    def __init__(self, value):
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

print("d1's instance variable is equal to:", d1.instance_var)
print("d2's instance variable is equal to:", d2.instance_var)
```

- [Refer q3.py](q3.py)


## Class Variables 

- The variables used at the class level are referred to as **class variables**.
- Class variables are defined within the class construction, so these variables are available before any class instance is created.
- To get access to a class variable, simply access it using the class name, and then provide the variable name.
- Similarly to instance variables, class variables are shown in the class's `__dict__` dictionary.

```python
class Demo:
    class_var = 'shared variable'

print(Demo.class_var)
print(Demo.__dict__)
```

- [Refer q4.py](q4.py)
