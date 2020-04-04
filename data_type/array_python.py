import array

# create
arr0 = array.array('i', [1, 2, 3])
print('\narray created by array.array:', arr0)

for i in range(0, 3):
    print('elements in array:', arr0[i], end = '\n')

arr0.append(100)
print('append to the end of array:', arr0)

arr0.insert(0, 1000)
print('insert a number to a specific position of array:', arr0)

# remove
arr1 = array.array('i', [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
last_element = arr1.pop(-1)
print('\nlast element is deleted in array:', last_element)
print('array after remove by pop():', arr1)
arr1.remove(2)
print('remove 1st occurrence of the value mentioned in its arg:', arr1)

# index
arr2 = array.array('u', ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'f', 'g'])
index = arr2.index('b')
print('\nreturn the 1st position of value mentioned in arg:', index)

# reverse
reverse = arr2.reverse()
print('\nassign a variable to arr2.reverse()', reverse)
print('array after reversing:')
for i in range(len(arr2)):
    print(arr2[i], end=' ')

# typecode, itemsize, buffer infor
arr3 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print('\n\ndata type of array:', arr3.typecode)
print('size in bytes of a single array element:', arr3.itemsize)
print('a tuple representing the address in which array is stored and number of elements:', arr3.buffer_info())

# count()
arr4 = array.array('i', [1, 1, 2, 1, 1, 2, 3, 2])
print('\n')
for i in range(4):
    print('the occurrence of %d in array:' % i, arr4.count(i))

# extend()
arr5 = array.array('i', [1000, 999, 888])
arr4.extend(arr5)
print('\nadd arr5 to arr4:', arr4)
arr6 = array.array('u', ['a', 'b', 'c'])
# arr5.extend(arr6)
# print('extend arr by arr5:', arr5)

# fromlist(list)
arr7 = array.array('i', [1, 2, 3, 1, 2, 5])
list0 = [0, 0, 0]
arr7.fromlist(list0)
print('\nadd a list to the end of array:', arr7)

# tolist
print('\nconvert array to a list:', arr7.tolist())