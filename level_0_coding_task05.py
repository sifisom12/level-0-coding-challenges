import math

# Task 0.5
# Calculating the area of a triangle using the semiperimeter method

def area_of_a_triangle (side1, side2, side3):
    sp = 1/2 * (side1 + side2 + side3)
    Area = math.sqrt(sp * ((sp - side1) * (sp - side2) * (sp - side3)))
    return Area

area = area_of_a_triangle (7, 9, 11)
print("Area is equal to " + "{:.2f}".format(area) + " square units")

