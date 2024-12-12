# Kaedon Ware
# 11/12/24
# P5Lab
# Simulate self-checkout using functions

# Import the random library to use in the program
import random 

 
def disperse_change(change):
    print(f"Change owed:.2f")
        # Convert money to a whole number
    change = int(change * 100)

    if change == 0:
         print("No change")
   

    # May need to round this value
    #money = round(money * 100)
    #print(money)

    # Get whole dollars from money amount
    dollars = change // 100
    #print(f"Dollars: {dollars}")

    # Remove the dollar amount from money
    money = chnage - (dollars * 100)


    # Get quarters from money amount
    quarters = change // 25
    #print(f"Quarters: {quarters}")

    # Remove the quarter amount from money
    change = change - (quarters * 25)

    # Get dimes from money amount
    dimes = change // 10
    #print(f"Dimes: {dimes}")

    #Remove dimes from money
    change = change - (dimes * 10)

    #Get the nickels from money
    nickels = money // 5
    #print(f"Nickels: {nickels}")

    # Remove nickels from money
    money = money - (nickels * 5)      

    # Get pennies from money amount
    pennies = money
    #print(f"Pennies: {pennies}")      

    if dollars >= 1 :
    if dollars == 1 :
        print(f"{dollars} dollar")
    else: # more than one dollar
        print(f"{dollars} dollar")

    if quarters >= 1 :
    if quarters == 1 :
        print(f"{quarters} quater")
    else: # more than one quarter
        print(f"{quarters} quaters")

    if dimes >= 1 :
    if dimes == 1 :
        print(f"{dimes} dime")
    else: # more than one dime
        print(f"{dimes} dime")
        
    if nickels >= 1 :
    if nickels == 1 :
        print(f"{nickels} nickel")
    else: # more than one dollar
        print(f"{nickels} nickel")        

    if dollars >= 1 :
    if dollars == 1 :
        print(f"{pennies} penny")
    else: # more than one dollar
        print(f"{pennies} pennies")




# Define the main function
 def main():
    print("Welcome to the store!")
    # Generate money owed
    owed = round(random.uniform(0.01,100.00),2)
    print(f"You owe ${owed:.2f}")
    inPut = float(input("How much cash will you put in the self checkout? $"))
    change = inPut - owed
    change = round(change, 2)

    #Call the function to show change as coins
    disperse_change(change)

# Call the main
if __name__ == "__main__":
    main()
    
    
    
