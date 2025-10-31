

unit = input("Is this weather in Celsius or Fahrenheit (C or F)?: ")

temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = (9 * temp)/5 + 32
    print(f"The temperature in Fahrenheit is: {round(temp, 1)} F")
elif unit == "F":
    temp = (temp - 32) * (5/9)
    print(f"The temperature in Celsius is: {round(temp, 1)} C")
else:
    print(f"{unit} is a not a valid unit of temperature")

