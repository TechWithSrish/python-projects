print("Welcome to the tip calculator !")
bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip /100
tip_amount = bill * tip_percentage
total_bill= bill + tip_amount

amount_per_person=  total_bill / people
print(f"Each person should pay: ${round(amount_per_person,2)}")


