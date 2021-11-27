# To calculate the area of a circle find the radius (rad).
# (The radius of a circle is the distance from the center of the circle to any point on its circumference.)
# area = rad squared * pi
# for circle(c) the radius is 10
# area_circle_c = (10 * 10 * math.pi)

import math

def area_of_circle(r):
    areaOfCircle = r**2 * math.pi
    return areaOfCircle

r = 10
result = area_of_circle(r)
print("The area of the circle is", result)



