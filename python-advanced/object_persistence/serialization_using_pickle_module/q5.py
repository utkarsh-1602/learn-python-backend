import pickle

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print(type(bytes))
print(bytes)

b_list = pickle.loads(bytes)
print(type(b_list))
print(b_list)
