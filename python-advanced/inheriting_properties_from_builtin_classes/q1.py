class CustomList(list):
    def __init__(self, *args):
        super().__init__(*args)  # Calls the __init__ method of list superclass

    def get_sum(self):
        return sum(self) # sum() python's built-in method sum to calculate sum of all elements of list
    
# Creating an instance of CustomList 
my_list = CustomList([1,2,3,4,5])

# Using inherited method from list 
my_list.append(6)
print("Extended List: ", my_list)

print("Sum of List: ", my_list.get_sum())
    
