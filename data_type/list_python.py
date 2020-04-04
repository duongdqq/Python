# Create a list
list0 = []
print(list0)

list1 = ['Today is 2nd day of learning python']
print(list1)

list2 = ['abc', 'def', 'ghi']
print(list2)

list3 = [[123, 456], [789, 101]]
print(list3)

list4 = [1, 2, 1, 2, 4, 4, 5, 5, 5]
print(list4)

list5 = [1, 'a']
print(list5, '\n')

# append() built in function
add0 = []
print(add0)
add0.append(1)
print(add0)
add0.append(2)
print(add0)

for i in range(3, 11):
    add0.append(i)
print(add0)

add0.append((11, 12))
print(add0)

add0.append([11, 12])
print(add0)

# insert() built in function
add0.insert(2, 1000)
print(add0)

# extend() built in function
add0.extend([1, 2, 3])
print(add0)

# Access elements form a list
add1 = ['a', 'b', 'c', 'd']
for i in range(0, 4):
    print('Value of %d index:' % i, add1[i])
add2 = [[1, 2, 3],
        [4, 5, 6]]
print(add2)
for i in range(0, 2):
    for j in range(0, 3):
        print(add2[i][j])

add3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(-1, (-len(add3) - 1), -1):
    print(add3[i])

# remove()
add4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
add4.remove(10)
print(add4)
for i in range(6, 10):
    add4.remove(i)
print(add4)

# pop()
add5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add5.pop())
print(add5)
add5.pop(0)
print(add5)

# Slice a list
add6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add6[3:7])
print(add6[7:])
print(add6[:])
print(add6[:1])

print(add6[-1:])
print(add6[-5:-1])
print(add6[::-1])
