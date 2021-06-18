# Task 0.6

def maximum_number(num1, num2, num3):
    if num1 > num2 and num1 >num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(maximum_number(221, 761, 2290))

def maximum_number(*nums):
    return max

maximum_number(7, 13, 78, 98, 107, 67)