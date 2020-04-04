# Create tuple
tuple0 = ()
tuple1 = (1, 2, 'abc')

list0 = [1, 2, 3, 'bcd']
tuple2 = tuple(list0)
print(tuple2)

tuple3 = tuple('Dang Quy Duong')
print(tuple3)

tuple4 = (1, 2, 3)
tuple5 = ('a', 'b', 'c')
tuple6 = (tuple4, tuple5)
print(tuple6)

tuple7 = ('Damn',) * 5
print(tuple7)

tuple8 = ('Heloo',)
n = 5
for i in range(n):
    tuple8 = (tuple8,)
    print(tuple8)

# Access tuple
tuple9 = tuple('abcdefghij')
print(tuple9)
print(tuple9[2])

tuple10 = ('Today', 'is', 'a wonderful day')
a, b, c = tuple10  # unpack tuple
print(a)
print(b)
print(c)

# Concatenate tuple
tuple11 = (1, 1, 1)
tuple12 = ('a', 'b')
print(tuple11 + tuple12)

# Slide tuple
tuple13 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple13[:])
print(tuple13[3:5])
print(tuple13[3:])
print(tuple13[::-1])

# Delete tuple
# Delete tuple
del tuple13
# print(tuple13)

