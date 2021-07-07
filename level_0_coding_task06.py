def maximum_number(num1, num2, num3):
    if num1 > num2 and num1 >num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(maximum_number(10000, 11761, 2290))

def maximum_number(*nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(maximum_number(985, 200, 8999, 19877, 111107, 4500))