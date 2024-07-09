# Deep copy 

import copy

original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)

original_list[2][0] = 'Changed'
print(original_list) 
print(deep_copy)   
