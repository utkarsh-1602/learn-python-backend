# Loops in python 

1. for Loop
- A for loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). This loop iterates over each element in the sequence and executes the block of code within the loop for each element.


- [refer q1.py](q1.py)

```python
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
```

- the `in` keyword introduces a syntax element describing the range of possible values being assigned to the control variable;
- the `range()` function (this is a very special function) is responsible for generating all the desired values of the control variable

```python 
for i in range(100):
    # do_something()
    pass
```


2. while loop
- A while loop executes a block of code as long as a specified condition is true. It repeatedly checks the condition before executing the loop's body.
- [refer q2.py](q2.py)

```python
count = 0
while count < 5:
    print(count)
    count += 1

```


## Loop Control Statements
- Python provides several control statements to modify loop behavior:

1. break: Terminates the loop prematurely.
2. continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
3. else: Executes a block of code once when the loop condition is no longer true (for while loops) or when the loop has iterated over all items (for for loops), unless terminated by a break statement.

- Using break to exit a loop
- [refer q3.py](q3.py)
```python
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

## Nested Loops
You can also nest loops, which means having a loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

```

## 