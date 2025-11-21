# Match case = Switch case

#Example 1
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: #Else or default clause
            return "Not a valid day"

print(day_of_week(2))
print(day_of_week(4))
print(day_of_week("Hola"))

#Example 2
def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
            return "It is "
        case "Wednesday":
            return False
            return "It is "
        case "Thursday":
            return False
        case "Friday":
            return True
        case "Saturday":
            return True
        case _: #Else or default clause
            return "Not a valid day"

print(is_weekend("Monday"))
print(is_weekend("Friday"))
print(is_weekend("Sunday"))
print(is_weekend("Wednesday"))
print(is_weekend("Hola"))

#Example 3 (with OR logical operator)
def is_weekend(day):
    match day:
        case "Friday" | "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday":
            return False
        case _: #Else or default clause
            return "Not a valid day"

print(is_weekend("Monday"))
print(is_weekend("Friday"))
print(is_weekend("Sunday"))
print(is_weekend("Wednesday"))
print(is_weekend("Hola"))


