# create a dictionary by manual
dict1 = {1: 'duong', 2: 'dang', 4: '123', 3: 'quy', 3: 3}
print(dict1)
dict2 = {'Today': 'Monday', 1: [1, 2, 3]}
print(dict2)
dict3 = {}
print(dict3)

# create a dictionary by built in function
dict4 = dict({1: 2, 2: 3})
print(dict4)
dict5 = dict([(1, 'Geeks'), (2, 'For')])
print('create a dictionary with each item as a pair', dict5)

# nested dictionary
dict6 = {1: 'geek', 2: 'for', 3: {'a': 'welcome', 'b': 'to', 'c': 'geeks'}}
print('nested dictionary', dict6)

# add
dict3[0] = 'geeks'
dict3[3] = 'for'
dict3[2] = 1
print('add elements one at a time', dict3)

dict3[1] = 'tom', 'yeu', 'ca', 'nha'
print('add set of values to a single key', dict3)

# update existing key's value
dict3[0] = 'update'
print('update existing key\'s value', dict3)

dict3[4] = {'nested': {'1': 'life', '2': 'geek'}}
print(dict3)

# accessing elements from a dictionary
print('access dictionary by key', dict3[4]['nested'])

# accessing by get()
print('access by get()', dict3.get(2))

# remove elements by del
dict7 = {5: 'Welcome', 6: 'To', 7: 'Geeks',
         'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
         'B': {1: 'Geeks', 2: 'Life'}}

del dict7[5]
print(dict7)

del dict7['B'][2]
print(dict7)

# remove by pop()
dict8 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = dict8.pop(1)
print('dictionary after pop()', dict8)
print('value associated to poped key', pop_ele)

# remove by popitem
dict9 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele1 = dict9.popitem()
print("dictionary after deletion: ", dict9)
print("the arbitrary pair returned is: ", pop_ele1)

# clear all dict
dict9.clear()
print(dict9)
