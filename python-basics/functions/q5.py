# Its data doesn't represent any reasonable value ‒ actually, it's not a value at all; hence, it mustn't take part in any expressions.


def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))

