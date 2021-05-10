
#Dictionary
#It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#  dictionaries are not lists - they don't preserve the order of their data, as the order is completely meaningless (unlike in real, paper dictionaries). The order in which a dictionary stores its data is completely out of your control, and your expectations. That's normal. (*)

# (*) In Python 3.6x dictionaries have become ordered collections by default. Your results may vary depending on what Python version you're using.

# And now the most important news: you mustn't use a non-existent key. Trying something like this:
#print(phone_numbers['president']) #throws error


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


#Iterating
# dict.keys() returns an iterable object consisting of all the keys gathered within the dictionary. 
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key]


#sorted keys:
# for key in sorted(dictionary.keys()):

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key in dictionary:
    print(key)

#Items & Values methods
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

#Modifying dictionary (If key already exists, it will modify its value else add new item)
# replace exising value
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)

# add new value
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

# add new value using update method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

# removing a key => del instruction
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog'] #(removing non existing key will throw error)
print(dictionary)

#removing all items
dictionary.clear()

#To copy a dictionary, use the copy() method:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
d2 = dictionary.copy()

# remove last item from dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}