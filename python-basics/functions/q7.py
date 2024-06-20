# There's a special Python method which can extend a variable's scope in a way which includes the function's body (even if you want not only to read the values, but also to modify them).Such an effect is caused by a keyword named global.

# Using this keyword inside a function with the name (or names separated with commas) of a variable (or variables), forces Python to refrain from creating a new variable inside the function ‒ the one accessible from outside will be used instead.

# In other words, this name becomes global (it has global scope, and it doesn't matter whether it's the subject of read or assign).


def my_fun():
    global a
    a = 2
    print(a)

a = 1
my_fun()
print(a)