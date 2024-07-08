# Exceptions in python

- Python comes with **63*** built-in exceptions, and they can be represented in the form of a **tree-shaped** hierarchy. The reason for this is that exceptions are inherited from BaseException, the most general exception class.

## Exception chaining 

- Exception Chaining in Python is a technique used to link multiple exceptions together, allowing one exception to be raised while preserving the context of the original exception.
- This is useful for debugging and understanding the sequence of errors that led to the final exception.
- When an error occurs and a new exception is raised in response, exception chaining helps to maintain a clear traceback of both the initial and subsequent exceptions.

### Implicit Exception Chaining 

- Implicit chaining happens automatically when an exception is raised inside an `except` block.
- Python captures the original exception and chains it with the new one.

```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("A value error occurred")
```

When you run this code, Python automatically chains the `ZeroDivisionError` with the `ValueError`.

## Explicit Exception Chaining

Explicit chaining gives you more control and clarity by explicitly specifying the original exception using the from keyword.

```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("A value error occurred") from e

```

In this case, the `ValueError` is explicitly linked to the `ZeroDivisionError`, making it clear that the `ValueError` was raised due to the `ZeroDivisionError`.


- This chaining concept introduces two attributes of **exception instances**:

1. the `__context__` attribute, which is inherent for implicitly chained exceptions.
2. the `__cause__` attribute, which is inherent for explicitly chained exceptions.


### Traceback attribute 

Python allows us to operate on the traceback details because each exception object (not only chained ones) owns a `__traceback__` attribute.
