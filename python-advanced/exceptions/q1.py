try:
    print(int('a'))
except ValueError as x:
    print(x.args)