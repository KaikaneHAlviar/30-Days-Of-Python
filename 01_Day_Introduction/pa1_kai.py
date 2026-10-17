import sys
import math

# Single-line comment

""" This is a multi-line comment 
    MuLti-line comments"""

# String
'This is a string'

# Boolean
True

# List
[0, 1, 2, 3, 4,5]

# Dictionary
{
'first name':'Kai',
'last_name':'Alviar',
'country':'United States',
'age':20,
'is_married':False,
'skills':['Eating', 'Slorking', 'Johnny']
}

# Tuple
('Earth', 'Jupiter', 'Neptune', 'Mars')

# Set
{2, 3, 4, 5}

# Exercise 2

# 1 Check python version
print(sys.version)

# 2 Operations
print(3 + 4)
print(4 - 3)
print(4 * 3)
print(4 % 3)
print(4**3)
print(4//3)

# 3 Print Strings
print('Kai')
print('Alviar')
print('United States')
print('I am NOT enjoying 30 days of python')

# 4 Check Data Types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Kai', 'Alviar']))
print(type('Kai'))
print(type('Alviar'))
print(type('United States'))


# Exercise 3

# Integer
print(3)
# Double
print(4.3)
# Complex
print(3+3j)
# String
print('Kai')
# Boolean
print(True)
# List
print([1,2,3,4])
# Tuple
print(('Earth', 'Jupiter', 'Neptune'))
#Dictionary
my_dict = {
'first name':'Kai',
'last_name':'Alviar',
'country':'United States',
'age':20,
'is_married':False,
'skills':['Eating', 'Slorking', 'Johnny']
}
print (my_dict)

print({
'first name':'Kai',
'last_name':'Alviar',
'country':'United States',
'age':20,
'is_married':False,
'skills':['Eating', 'Slorking', 'Johnny']
})

# Finding Euclidean Distance
def euclidean_distance(p1, p2):
    return(math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2))

print(euclidean_distance((2,3), (10,8)))











def euclidean_distance2(p1, p2):
    print(math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2))



euclidean_distance2((2,3), (10,8))