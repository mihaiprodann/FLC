import datetime
import math
import random

#Ex 1
print(datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M%p"))

#Ex 2
radius = int(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is: ", area)

#Ex 3
mylist = [1, 2, 3, 4, 5]
print("A random number from the list is: ", random.choice(mylist))

#Ex 4
print("The shuffled list is: ")
random.shuffle(mylist)
print(mylist)

#Ex 5
nr1 = int(input("Enter the first number: "))
nr2 = int(input("Enter the second number: "))

print("The least common multiple of the two numbers is: ", math.lcm(nr1, nr2))
print("The greatest common divisor of the two numbers is: ", math.gcd(nr1, nr2))

#Ex 6
nr = int(input("Enter a number: "))
print("The factorial of the number is: ", math.factorial(nr))

#Ex 7
date = datetime.datetime.now()
print("The week number of the date is: ", date.isocalendar()[1])

#Ex 7 write a program that computes the distance between two points
x1 = int(input("Enter the x coordinate of the first point: "))
y1 = int(input("Enter the y coordinate of the first point: "))
x2 = int(input("Enter the x coordinate of the second point: "))
y2 = int(input("Enter the y coordinate of the second point: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("The distance between the two points is: ", distance)