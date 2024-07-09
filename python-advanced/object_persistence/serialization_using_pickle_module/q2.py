import pickle
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Define the data
data = {'name': 'Alice', 'age': 23, 'city': 'New York'}

# Serialize the data to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
