dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)


dictionary['cat'] = 'minou'
print(dictionary)
