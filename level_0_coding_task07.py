def fahrenheit_to_celsius(temperature):
    converted_temp = (temperature - 32) * 5/9
    return converted_temp

celsius = fahrenheit_to_celsius(145)
print("{:.2f}".format(celsius) + "°C")


def celsius_to_fahrenheit(temperature):
    converted_temp = (temperature * 9/5) + 32 
    return converted_temp

farenheit = celsius_to_fahrenheit(42)
print("{:.2f}".format(farenheit) + "°F")


