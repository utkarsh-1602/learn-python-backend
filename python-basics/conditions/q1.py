# Python uses boolean logic to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


# if statement
statement = False
another_statement = True
if statement is True:
    print("statement is True")
    pass
elif another_statement is True: # else if
    print("another statement is True")
    pass
else:
    print("something is False")
    pass


# is operator
# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.

x1 = [1,2,3]
y1 = [1,2,3]
print("\n")
print(x1 == y1)
print(x1 is y1) 


# and, or operator
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list.
name2 = "utkarsh"
if name2 in ["John", "utkarsh"]:
    print("Your name is either John or utkarsh.")


# not operator 
print(not False) # Prints out True
print((not False) == (False)) # Prints out False