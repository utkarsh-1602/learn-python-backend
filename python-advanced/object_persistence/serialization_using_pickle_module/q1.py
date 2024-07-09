import pickle

data = {'name': 'Alice', 'age': 23, 'city': 'New York'}

# Serialize the object to a bytes object
data_bytes = pickle.dumps(data)

print(data_bytes)