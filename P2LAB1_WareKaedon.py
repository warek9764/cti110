# Kaedon Ware
# 9/30/2024
#P2LAB1
# Using Import Libraries , math , and f string

# Import math library
import math

#Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate diameter
diameter = 2 * radius

# Display diameter with one  decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumference
circum = 2 * math.pi * radius

# Display circumference with two decimal place
print(f"The circumference of the circle is {circum:.2f}\n")

#Calculate the area
area = math.pi * (radius ** 2)

#Display the area
print(f"The area of the circle is {area:.3f}")

