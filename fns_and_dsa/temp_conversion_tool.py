FAHRENHEIT_TO_CELSIUS_FACTOR = 9/5
CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9

# Formular (x - 32) x (5/9) where x is fahrenheit
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return f"{fahrenheit}°F is {celsius}°C"

# Formular (x * (9/5)) + 32 where x is celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
    return f"{celsius}°C is {fahrenheit} °F"

temperature = input("Enter the temperature to convert: ")
type_of_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature.isnumeric() == False:
    print("Invalid temperature. Please enter a numeric value.")

# Makes the string into a valid number
temperature = int(temperature)

if type_of_temperature == "F":
    print(convert_to_celsius(temperature))
elif type_of_temperature == "C":
    print(convert_to_fahrenheit(temperature))
else:
    print("Invalid symbol enter C or F")


