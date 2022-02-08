print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_people = int(input("How many people to split the bill? "))

tip = (tip_percentage / 100) * total_bill

bill_per_person = ((total_bill + tip) / number_people)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final _amount}.")

