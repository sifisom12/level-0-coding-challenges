# Task 0.8

def number_to_time(number):
        hours = number // 60
        minutes = number % 60
        return hours, minutes

time = number_to_time(122)

print(f"Time equals {time[0]} hour(s) and {time[1]} minute(s)")