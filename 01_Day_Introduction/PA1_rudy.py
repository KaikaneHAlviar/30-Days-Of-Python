import math 

print(1 + 2)            # addition(+)
print(1 - 2)            # subtraction(-)
print(1 * 2)            # multiplication(*)
print(1 / 2)            # division(/)
print(1 ** 2)           # exponential(**)
print(1 % 2)            # modulus(%)
print(1 // 2)           # Floor division operator(//)

# Checking data types
print(type(10))                 # Int
print(type(3.14))               # Float
print(type(1 + 3j))             # Complex number
print(type('rudy'))             # String
print(type([1, 2, 3]))          # List
print(type({'name':'rudy'}))    # Dictionary
print(type({9.8, 3.14, 2.7}))   # Set
print(type((9.8, 3.14, 2.7)))   # Tuple

print('rudy')
print('ramirez')
print('U.S')
print('I am enjoying30 days of python')

print(20)
print((5.29))
print(9 + 5j)
print('rudy')
print(True or False)
print([2, 4, 6])
print((9.1, 4.6, 8.1))
print({5.2, 6.5, 7.9})

print({
    'first_name':'rudy', 'last_name':'ramirez', 'country':'U.S', 'age':99, 
    'is_married':False, 'skills':['living', 'walking', 'rule34dle', 'hey peter']
})

print(math.sqrt((10 - 2)**2 + (8 - 3)**2))

def euclidean_distance2(p1, p2):
    print(math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2))

euclidean_distance2((5,8), (20,6))