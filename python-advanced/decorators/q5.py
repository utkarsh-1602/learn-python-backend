def warehouse_decorator(material):
    def wrapper(fun01):
        def internal_wrapper(*args):
            print('wrapping items from {} with {}'.format(fun01.__name__, material))
            fun01(*args)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Rich Dad Poor Dad', "The Richest Man in Babylon")
pack_toys('bike', 'car')
pack_fruits('apple', 'banana')
