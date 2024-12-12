# Kaedon Ware
# 10/2/2024
# P2LAB2
# Using dictionaries

#Create dictionary
vehicles = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado": 26}

#Print all keys in dictionary
print(vehicles.keys())
print()

#Get a car (key) from user
userCar = input("Enter a vehicle to see it's MPG: ")
print()

#Display mpg for users car
print(f"The {userCar} gets {vehicles[userCar]} mpg.")
print()
# Promt user to enter number of miles
miles_to_drive = int(input(f"How many miles would you like to drive the {userCar}? "))
print()

# Calculate Gallons of Gas needed
gallons_needed = miles_to_drive/vehicles[userCar]

#Display gallons of gas needed
print(f"{gallons_needed:.2f} gallon(s) are needed to drive the {userCar} miles.")
