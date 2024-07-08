class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')
  
    def __setitem__(self, index, value):
        IntegerList.check_value_type(value) # condition 
        list.__setitem__(self, index, value)

    # __setitem__() is a special method used for assignment to an index in an object. It is invoked when you use square brackets ([]) to assign a value to an index in an object, typically in sequence-like objects such as lists, dictionaries, or custom classes that implement this method.

    def append(self, value):
        IntegerList.check_value_type(value) # condition
        list.append(self, value)

    def extend(self, temp_list):
        for i in temp_list:
            IntegerList.check_value_type(i) # condition
        
        list.extend(self, temp_list)


int_list01 = IntegerList()
print(int_list01)

int_list01.append(10)
int_list01.append(20)
int_list01.append(30)
print(int_list01)

int_list01[0] = 100
print(int_list01)

int_list01.extend([5,6,7,8])
print(int_list01)


try:
    int_list01.append('8-10')
except ValueError:
    print('Appending string failed')

try:
    int_list01[0] = '10/11'
except ValueError:
    print('Inserting string failed')

try:
    int_list01.extend([997, '10/11'])
except ValueError:
    print('Extending with ineligible element failed')
