# Method 1:
'''
#Welcome Message
print("Welcome to the tip calculator")

#Ask user to enter total amount of bill
bill = float(input("What was the total bill?"))

#Ask user to enter what percentage tip they want to add
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_bill = int((bill) + (bill * (tip)/100))

#Ask user to add total number of people
total_people = int(input("How many people to split the bill?"))

#calculate the per person share.
person_bill = round(int(total_bill) / int(total_people),2)
print(f"Each person shoud pay: ${person_bill}")

'''


# Method 2 (Less Coding):

#Welcome Message
print("Welcome to the tip calculator")

#Ask user to enter total amount of bill
bill = float(input("What was the total bill?"))

#Ask user to enter what percentage tip they want to add
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))

#Ask user to add total number of people
total_people = int(input("How many people to split the bill?"))

tip_amount = (bill * (tip)/100) # Calculating only tip amount

print(f"Each person should pay: ${round((bill + tip_amount) / (total_people),2)}")