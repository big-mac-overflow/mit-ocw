# Part A: House Hunting

# PSEUDOCODE
# User gets salary,
# sets aside a part of it
# invests this part
# gets monthly return on investment
# this return + the salary they earn in that month is invested again
# process continued until they have saved enough for the house

annual_salary = float(input('Enter your annual salary: '))                              # taking input of user's annual salary and casting it into float
portion_saved = float(input('Enter the portion of salary save(as a decimal): '))        # taking input of the portion of salary, user wants to set aside to buy house and casting it into float
total_cost = float(input('Enter the cost of your dream home: '))                        # taking input of total cost of house and casting it into float

portion_down_payment = 0.25                                                             # the down payment user has to pay (equal to 25% of total cost of house)
down_payment = total_cost * portion_down_payment                                        # Calculating the down payment on the house

current_savings = 0                                                                     # initially, there are no savings
no_of_months = 0                                                                        # setting counter = 0

r = 0.04                                                                                # given rate of return

monthly_saving_from_salary = (annual_salary/12) * portion_saved                         # amount of money user is setting aside on a MONTHLY basis from their salary

while current_savings < down_payment:                                                   # user needs to save money until they have equal or more than the down-payment
    current_savings += monthly_saving_from_salary + ((current_savings) * r / 12)        # refer PSEUDOCODE
    no_of_months += 1                                                                   # incrementing counter by one

print('Number of months: ', no_of_months)
