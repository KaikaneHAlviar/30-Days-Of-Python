import math

age = 20
height = 5.8
complex = 1 + 1j

def calculate_triangle():
    base = float(input('enter base: '))
    height = float(input('enter height: '))
    return print('The area of the triangle is', 0.5 * base * height)

def calculate_perimeter():
    a = float(input('Enter side a: '))
    b = float(input('Enter side b: '))
    c = float(input('Enter side c: '))
    return print('The perimeter of the triangle is', a + b + c)

def caclulate_rectangle():
    width = float(input('Enter width: '))
    length = float(input('Enter height: '))
    print('The area of the rectangle is', length * width)
    print('The perimeter of the rectangle is', 2 * (length * width))
    return

def calculate_circle():
    pi = math.pi
    radius = float(input('Enter the radius: '))
    print('The area of the circle is', pi * (radius**2))
    print('The circumference of the circle is ', 2 * pi * radius)

def q_8():
    equ = input('Input equation in y = mx + b format: ') #y = mx + b
    
    m = float(equ[4])
    b = float(equ[9])
    print('The slope is', m)
    print('The x-intercept is', -b / m)
    print('The y-intercept is', m * 0 + b) # doesnt work with - 
    return m

def q_9():
    x1, y1 = map(float, input("Enter 1st point x, y: ").split(','))
    p1 = (x1,y1)
    x2, y2 = map(float, input("Enter 2nd point x, y: ").split(','))
    p2 = (x2,y2)
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

slope_1 = 0 # q_8()
slope_2 = 0 # q_9()
if slope_1 > slope_2:
    print('Slope 1 is larger')
elif slope_2 < slope_1:
    print('Slope 2 is larger')
else:
    print('Both are the same')

def q_11():
    x = float(input('Enter x: '))
    return x**2 + 6 * x + 9 # y = 0 at x  = 3

p = 'python'
d = 'dragon'
pl = len(p)
dl = len(d)
compare = p[1] == d[1]

if 'on' in p and 'on' in d:
    print('on is in both words')

sentence = 'I hope this course is not full of jargon'
is_there = 'jargon' in sentence

string_convert = str(float(len('python')))

def is_even(x: int):
    if x / 2 == 0:
        return print(x, 'is even')
    else:
        return print(x, 'is odd')

q_18 = 7 // 3 == int(2.7)
q_19 = type('10') == type(10)
q_20 = int(float('9.8')) == type(10)\

def pay():
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate per hour: '))
    return print('Your weekly earning is ', hours * rate)

def age_in_seconds():
    age = int(input('Enter your age: '))
    return print('Youve lived for', age * 31556926, 'seconds')

def table():
    x = 0
    while x < 5:
        x += 1
        print(x,1,x,x**2,x**3)

table()