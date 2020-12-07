# Get total bill
total_bill: float = float(input('What is the total bill? $'))

# Get total number of people
number_of_people = int(input('How many people to split the bill? '))

# Get total percentage of tip
tip_percentage: float = float(input('What percentage tip would you like to give? 10, 12, or 15? '))
total_amount = total_bill * (1 + tip_percentage/100)

tip_per_person = total_amount / number_of_people
print(f'Each person should pay: ${round(tip_per_person, 1)}')