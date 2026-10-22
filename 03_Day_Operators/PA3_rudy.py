# import math

# # Calculating area of a circle
# radius = 10                                 # radius of a circle
# area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
# print('Area of a circle:', area_of_circle)

# # Calculating area of a rectangle
# length = 10
# width = 20
# area_of_rectangle = length * width
# print('Area of rectangle:', area_of_rectangle)

# # Calculating a weight of an object
# mass = 75
# gravity = 9.81
# weight = mass * gravity
# print(weight, 'N')                         # Adding unit to the weight

# # Calculate the density of a liquid
# mass = 75 # in Kg
# volume = 0.075 # in cubic meter
# density = mass / volume # 1000 Kg/m^3
# print(density, 'Kg/m^3') # Adding unit to the density

# age = 10
# height = 5.5
# store = 3j

# # Area of triangle
# base = int(input('enter base:'))
# height = int(input('enter height:'))
# area_of_triangle = 0.5 * base * height
# print(area_of_triangle)

# # perimiter of triangle
# side_a = int(input('enter side_a:'))
# side_b = int(input('enter side_b:'))
# side_c = int(input('enter side_c:'))
# perimiter = side_a + side_b + side_c
# print(perimiter)

# #perimiter/area of rectangle
# length = int(input('enter length:'))
# width = int(input('enter width:'))
# area_of_rectangle = length * width
# perimiter_of_rectangle = 2*(length + width)
# print(area_of_rectangle)
# print(perimiter_of_rectangle)

# #area/cirdumference of circle
# radius = int(input('enter raduis:'))
# math.pi
# area_of_circle = math.pi * radius * radius
# ccircumference = 2 * math.pi * radius
# print(area_of_circle)
# print(ccircumference)

# #slope and euclidian distance 
# y = 2*2 - 2
# print(y)

# y1=2
# y2=10
# x1=2
# x2=6
# m = y2 - y1 / x2 - x1
# print(m)

# print(math.sqrt((10 - 2)**2 + (6 - 2)**2))

# def euclidian_distance(p1, p2):
#     print(math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2))

# euclidian_distance((6,10),(2,2))

# x = int(input('enter x:'))
# y = x**2 + 6 * x + 9
# print(y)

# print(len('python') == len('dragon'))
# print(len('python') > len('dragon'))
# print('on' in 'python', 'on' in 'dragon')
# print('jargon' in 'i hope this course is not full of jargon')
print('on not in python', 'on not in dragon', 'on' not in 'python/dragon')
print(str(float(len('python'))))
if 10 % 2 == 0 :
    print('number is T')
print(int(2.7))
print(7 // 3)
print(7 // 3 == int(2.7))
print(type('10') == 'type of 10')
print(int(9.8) == type(10))

hours = int(input('enter hours:'))
rate_per_hour = int(input('enter rate_per_hour:'))
weekly_earnings = hours * rate_per_hour
print(weekly_earnings)

x = 0
while x < 5:
    x += 1
    print(x,1,x,x**2,x**3)