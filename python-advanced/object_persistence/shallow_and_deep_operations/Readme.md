# Shallow and deep operations in python 

- In Python, "**shallow**" and "**deep**" operations generally refer to how objects are copied or assigned.
- Understanding these concepts is crucial, especially when dealing with mutable data structures like lists or dictionaries.

## Shallow copy 

- A shallow copy of an object is a new object that is a copy of the original object, but it only copies the references to the objects found in the original.
- This means that if the original object contains other objects (like lists within a list), the shallow copy will refer to the same objects, not new copies of those objects.
- When you create a shallow copy of a list, the new list (the shallow copy) gets its own references to the same objects contained in the original list. This means:
    - The new list itself is a new object.
    - The elements inside the list are references to the same objects contained in the original list.


[Refer q1.py](./q1.py)


## Deep copy

- A deep copy of an object is a new object that is a copy of the original object, and it recursively copies all objects found in the original.
- original. This means that even if the original object contains other objects, the deep copy will contain copies of those objects, not references to the original ones.


[Refer q2.py](./q2.py)


## print Ids of variables 

[Refer q3.py](.q3.py)
