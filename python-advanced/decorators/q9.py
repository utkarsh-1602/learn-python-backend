class storeDecorator:
    def __init__(self, action):
        self.action = action

    def __call__(self, my_func):
        def wrapper(*args, **kwargs):
            print("My function name is {}, which does {}".format(my_func.__name__, self.action))
            my_func(*args, **kwargs)
            print()
        return wrapper
    

@storeDecorator('packing of books')
def pack_books(*args):
    print("Let's Pack this books: ", args)

pack_books('psychology of money', 'atomic habits')

@storeDecorator('managing the project')
def manage_project(**kwargs):
    print("The People that are managing the project are: ", kwargs)


manage_project(utkarsh='backend', tushar='frontend', radhe='devops', sameer='testing', omkar='support')