weight = float(input("Enter your weight: "))

unit = input("Kilograms or pounds? (KG or LBS): ")

if unit == "KG":
    weight *= 2.205
    print(f"Your weight in pounds is: {round(weight, 2)} lbs")
elif unit == "LBS":
    weight /= 2.205
    print(f"Your weight in kilograms is: {round(weight, 2)} kgs")
else:
    print(f"{unit} is a not a valid unit of weight")

