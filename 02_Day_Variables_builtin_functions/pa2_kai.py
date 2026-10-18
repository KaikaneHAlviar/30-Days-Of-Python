import math

# gives min value
min(20, 30, 40)

# gives max value
max(20, 30, 40)

# takes list and returns min
min([20, 30, 40])

# takes list and returns max
max([20, 30, 40])

#takes list and returns sum
sum([20, 30, 40])

# Variables

first_name = 'Kai'
last_name = 'Alviar'
age = 20
is_married = False
skills = ['trombone', 'celery']
personal_info = {
    'firstname': 'Kai',
    'lastname': 'Alviar',
    age: 20,
    'city': 'Puyallup'
}

print('Hello ', 'World')
print(len('Hello, World'))

# first_name, last_name, age = 'Kai', 'Alviar', 20

# Taking input from terminal
""" user_name = input('What is your username?: ')
user_age = input('How old are you?: ')
print(user_name)
print(user_age) """

print(type({'name': 'Kai Alviar'}))
print(type(zip([1, 2],[3, 4])))

# Converting Data Types

# int to float
num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int / float
num_str = '10.6'
num_float = float(num_str) # convert to float first
num_int = int(num_float) # then convert to int
print('num_int', num_int)      # 10
print('num_float', num_float)  # 10.6

# str to list
first_name = 'Kai'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)

# Integers are negative, zero, positive whole numbers
# Float are decimal numbers
# Complex numbers always in formula of a (+/-) bj

# Exercise 1
first_name = 'Kai'
last_name = 'Alviar'
full_name = first_name + ' ' + last_name
print(full_name)
country = 'United States'
city = 'Puyallup'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True
dictionary = {
    'firstname': 'Kai',
}
print(dictionary)

my_name, your_name = 'Kai', 'Rudy'

# Exercise 2
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(dictionary)

len(first_name)

if len(first_name) > len(last_name):
    print(first_name, 'longer')
elif len(first_name) < len(last_name):
    print(last_name, 'longer')
else:
    print(first_name, 'and', last_name, 'are the same length')

num_one = 5
num_two = 4
num_three = num_one + num_two
print(num_three)
test = 'test'
test2 = 'test2'
test3 = test + test2
print(test3)

num_four = num_one - num_two
num_five = num_one * num_two
num_six = num_one / num_two
num_seven = num_one % num_two
num_eight = num_one**num_two
num_nine = num_one // num_two

area_of_circle = math.pi * int(input('What is the radius?: ')) ** 2
print(area_of_circle)

try:
    user_dictionary = {
        'user_name': input('What is your first name?: '),
        'user_last': input('What is your last name?: '),
        'country': input('What is your country?: '),
        age: int(input('What is your age?: ')),
    }
except ValueError:
    print("Error: Age must be a valid integer.")

def circle_area(radius):
    return math.pi * radius**2

print('radius:')
# print(circle_area(30))
print(circle_area(int(input('What is the radius? '))))

def circle_circumference(radius):
    return 2 * math.pi * radius

print('circumference:')
# print(circle_circumference(30))
print(circle_circumference(int(input('What is the radius? '))))