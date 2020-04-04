# Create
set0 = set()
print(set0)

string0 = 'Hello World'
set1 = set(string0)
print(set1)

set2 = set('Hello World')
print(set2)

list0 = [1, 2, 3, 'a', 'b', 1, 2, 3, 'a', 'b', 'c']
set3 = set(list0)
print(set3)

# Add
set4 = set()
set4.add('a')
print('add a string to set4:', set4)
# set4.add(1, 2)
set4.add((1, 2, 4, 'a'))
print('add a tuple to set4:', set4)
# Cannot add a list to a set because list is not hashable
# set4 = set()
# set4.add([1, 2, 'a'])
# print('set4 =', set4)
for i in range(4):
    set4.add(i)
    print('add an element to set4 by loop for:', set4)

# Update
set5 = set()
set5.update([1, 2, 'a'])
print('update a list to set5', set5)
# Can update lists to a set
set5.update([1, 2], [3, 4], 'a', 'abc', (4, 5, 6, 'abc'))
print('update lists, strings, tuple to set5:', set5)

# Access
set6 = set([1, 2, 3, 3, 3, 'a', 'abc'])
print(set6)
for i in set6:
    print('access set6 by loop for:', i, end='\n')
print('abc' in set6)

# Remove
set7 = set([1, 2, 3, 4, 5])
set7.remove(1)
print('remove only one element by remove:', set7)
# set7.remove(10)
set7. discard(10)
print('remove an outside element by discard:', set7)
a = set7.pop()
print('remove a random last element by pop:', set7)
print('return the last element by pop:', a)
set7.clear()
print('clear a set:', set7)

# Frozen set
tuple0 = ('a', 'b', 'c', 'd', 'e')
Fset = frozenset(tuple0)
print('Frozenset:', Fset)
print('Empty Frozen set:', frozenset())

