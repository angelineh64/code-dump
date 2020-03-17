# Angeline Hidalgo
# February 2, 2020

miles_driven = input("How many miles have you driven: ")  # Prompts user to enter their mileage
miles_driven = float(miles_driven)
gallons_used = input("How many gallons are you using: ")  # Prompts the user to enter how many gallons they used
gallons_used = int(gallons_used)

mpg = gallons_used / miles_driven  # Calculates MPG by dividing gallons_used by miles_driven

if (mpg<25):
    print("Could do better!")  # Alerts user that improvement could be used when using gas.
if (mpg>25 and mpg<50):
    print("You are doing ok!")  # Alerts user that their gas usage is ok.
if (mpg>50):
    print("Excellent work!")  # Tells user that they're doing excellent with gas usage.

print("Your car's MPG is:", mpg, "gallons per mile")

