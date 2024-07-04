# Decorators in python 

- A decorator is one of the design patterns that describes the structure of related objects. Python is able to decorate functions, methods, and classes.
- The **decorator's** operation is based on wrapping the original function with a new "decorating" function (or class), hence the name "decoration". This is done by **passing the original function as a parameter to the decorating function** so that the decorating function can call the passed function. The decorating function returns a function that can be called later.
- Decorators are used to perform operations before and after a call to a wrapped object or even to prevent its execution, depending on the circumstances. As a result, we can change the operation of the packaged object without directly modifying it.


Decorators are used in:

    the validation of arguments;
    the modification of arguments;
    the modification of returned objects;
    the measurement of execution time;
    message logging;
    thread synchronization;
    code refactorization;
    caching.

[Refer q1.py](q1.py)


## @simple_decorator
- a simple decorator – a function which accepts another function as its only argument, prints some details, and returns a function or other callable object.

```python 
    def simple_decorator(function):
        print("We are about to call {}".format(function.__name__))
        return function

    @simple_decorator
    def simple_hello():
        print("Hello from simple function!")

simple_hello()    
```

[Refer q2.py](./q2.py)

[Refer q4.py](./q4.py)


## Decorators should be universal 
- When we say "decorators should be universal," we mean that the decorator should be capable of working with any function, regardless of the number and types of arguments that function accepts.
- This universality can be achieved by using the ***args** and ****kwargs** constructs, which allow the decorator to accept and pass through any number of positional and keyword arguments.


[Refer q3.py](./q3.py)


## Decorators can accept their own attributes 

- In Python, decorators can be made more flexible and universal by accepting arguments. This allows the same decorator to be used with different parameters, enhancing functionality without altering the core functions.

[Refer q5.py](./q5.py)
