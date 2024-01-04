# len operator : used to find the length
astring = "Hello world!"
print(len(astring))

# index operator : used to find the index
astring2 = "utkarsh"
print(astring2.index("s"))

# count operator : used to find the number of elements
astring3 = "Hello world!"
print(astring3.count("l"))

# slice a string
astring4 = "utkarsh learns python"
print(astring4[3:7])

# extended slice syntax
astring5 = "pythonprogramming"
print(astring5[3:10:2]) 
#This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].


# reverse a string 
astring6 = "Hello world!"
print(astring6[::-1])


# convert to uppercase and lowercase
astring7 = "Hello world!"
print(astring7.upper())
print(astring7.lower())


# returns a boolean value by checking startswith and endswith
astring8 = "Hello world!"
print(astring8.startswith("Hello"))
print(astring8.endswith("asdfasdfasdf"))


# splits the string into a bunch of strings grouped together in a list using split("")
astring9 = "Hello world!"
afewwords = astring9.split(" ")
print(afewwords)