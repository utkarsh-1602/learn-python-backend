# Metaprogramming in Python

- Metaprogramming is a programming technique in which computer programs have the ability to modify their own or other programs codes.
- Metaprogramming in Python refers to a programming technique where programs have the ability to treat other programs as their data. This means that a program can read, generate, analyze, or transform other programs, and even modify itself while running.
- Python supports metaprogramming through several features like `decorators`, `metaclasses`, and the introspection capabilities provided by the `inspect` module.

# Key concepts of metaprogramming

## Introspection

**Introspection** is the ability of a program to examine the type or properties of an object at runtime. In Python, you can use built-in functions like `type()`, `dir()`, `getattr()`, `hasattr()`, and the `inspect` module for introspection.

[Refer q1.py](./q1.py)

## Decorators

Decorators are a way to modify or enhance functions and methods without changing their definition. They are often used for logging, access control, memoization, and more.

[Refer q2.py](./q2.py)

## Metaclasses

Metaclasses are classes of classes. They define the behavior of classes and can be used to control class creation. The metaclass of a class is defined by setting the `__metaclass__` attribute.

It’s important to remember that metaclasses are classes that are instantiated to get classes.


[Refer q3.py](./q3.py)

## Dynamic Code Execution

Python allows the execution of dynamically generated code using `exec()` and `eval()` functions.

