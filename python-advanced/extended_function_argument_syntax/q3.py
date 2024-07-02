def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)

def super_combiner(my_c, *args, **kwargs):
    print("args: ", args)
    print("my_c: ", my_c)
    print("kwargs: ", kwargs)


combiner(1, 'b', 1,1, c=2, argument1=1, argument2='U')