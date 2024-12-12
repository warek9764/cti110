# Kaedon Ware
#10/13/24
# P2HW2

#Create list for modules
module = []
module_1 = float(input("Enter grade for Module 1:"))
module_2 = float(input("Enter grade for Module 2:"))
module_3 = float(input("Enter grade for Module 3:"))
module_4 = float(input("Enter grade for Module 4:"))
module_5 = float(input("Enter grade for Module 5:"))
module_6 = float(input("Enter grade for Module 6:"))

#Add Variables to the list
module.append(module_1)
module.append(module_2)
module.append(module_3)
module.append(module_4)
module.append(module_5)
module.append(module_6)

print("----------Results----------")
print(f"{'Lowest Grade:':<19} {min(module)}")
print(f"{'Highest Grade:':<19} {max(module)}")
print(f"{'Sum of Grades:':<19} {sum(module)}")
print(f"{'Average:':<19} {sum(module)/len(module ,.2f)}")
