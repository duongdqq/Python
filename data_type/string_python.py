# Create a string
# Use single quotes
single = 'Today is Wednesday April 1st 2020'
print('This is a string created by single quotes:', single)

# Use double quotes
double = 'I am learning how to code python'
print('This is a string created by double quotes:', double)

# Use triple quotes
triple = '''What a funny new!'''
print('This is a string created by triple quotes:', triple)

# Use triple quotes to have many lines
line = '''
        1
        2
        3'''
print('Create many lines with triple quotes:', line)

# Access characters in string
access = '2020 is my year'
print('A string:', access)
print('1st character:', access[0])
print('Last character:', access[-1])
print('Characters from 3th to 12th (index of string):', access[3:12])
print('Characters from 3th to 2nd last:', access[3:-2])

# Update a string
update = 'This is an initial string'
# String doesnt allow item assignment
# initial[0] = 1
# print('String after assigned item:', initial)
update = 'String after updated by assigned whole string'
print('String after updated by assigned whole string:', update)

# Delete a string
delete = 'Initial string'
# String doesnt allow item deleted
# del delete[2]
# print('String after deleted 2nd item:', delete)
# del delete
# print(delete)

# Escape sequencing a string
escape = '''I'm an Artificial Intelligent "engineer"'''
print('Escape by triple quotes:', escape)

escape1 = 'I\'m an Artificial Intelligent "engineer'
print('Escape by backslash:', escape1)

escape2 = "I'm an Artificial Intelligent \"engineer\""
print('Escape by backslash:', escape2)

escape3 = "D:\\duongdq\\darknet"
print('Escape by backslash:', escape3)

escape4 = 'This is \x47\x65\x65\x6b\x73 in \x48\x45\x58'
print(escape4)
escape4 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
escape5 = R"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print(escape4)
print(escape5)

# Format a string
format0 = '{} {} {}'.format('I', 'Luv', 'you')
print('Print string in default order:', format0)

format1 = '{2} {1} {0}'.format('I', 'Luv', 'you')
print('Print String in Positional order:', format1)

format2 = '{a} {c} {b}'.format(a = 'I', b = 'Luv', c = 'you')
print('Print String in order of Keywords:', format2)

format3 = '{0:b}'.format(2)
print('Binary representation of 16 is:', format3)

format4 = '{0:e}'.format(1234.5678)
print('Exponent representation of 165.6458 is:', format4)

format5 = '{0:.5f}'.format(1 / 17)
print('1 divide 17 is:', format5)

format6 = 123456.7891011
print('Formatting in 3.3f format:')
print('The value of format6 is: %.3f' % format6)

format7 = '{:0.3f}'.format(123456.7891011)
print('Formatting format7 by format:', format7)
