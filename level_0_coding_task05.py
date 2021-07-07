import math

def area_of_a_triangle (side1, side2, side3):
    """
    Calculating the area of a triangle using the semiperimeter method
    """
    semiperimeter = 1/2 * (side1 + side2 + side3)
    area = math.sqrt(semiperimeter* ((semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)))
    return area

area = area_of_a_triangle (7, 9, 11)
print("Area is equal to " + "{:.2f}".format(area) + " square units")

