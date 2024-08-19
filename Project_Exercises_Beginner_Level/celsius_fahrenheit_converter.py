def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


unit = input('Enter the temperature unit (C for Celsius, F for Fahrenheit): ')
value = float(input("Enter the temperature value to be converted: "))

if unit.upper() == "C":
    print(f"{value} Celsius is {celsius_to_fahrenheit(value):.2f} Fahrenheit.")
elif unit.upper() == "F":
    print(f"{value} Fahrenheit is {fahrenheit_to_celsius(value):.2f} Celsius. ")
else:
    print("Invalid temperature unit")
