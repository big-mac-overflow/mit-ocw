# Part B: Saving, with a raise

# SIMPLE PROBLEM DESCRIPTION
# every 6 months the annual salary is increased by a percentage given by semi_annual_raise(in decimal form), rest all factors stay the same

# SOLUTION
# if no_of_months % 6 == 0, calc. new salary by multiplying old salary with rate of increase and assign this value to the old salary
# put this if loop inside the while loop

annual_salary = float(input('Enter your starting annual salary: '))                              
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))        
total_cost = float(input('Enter the cost of your dream home: '))                        
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: ')) 


portion_down_payment = 0.25                                                            
down_payment = total_cost * portion_down_payment                                        

current_savings = 0                                                                     
no_of_months = 0                                                                       
r = 0.04                                                                               

monthly_saving_from_salary = ( annual_salary / 12 ) * portion_saved                        

while current_savings < down_payment:                                                   
    current_savings += monthly_saving_from_salary + ((current_savings * r) / 12)        
    no_of_months += 1    
    
    if no_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise  
        monthly_saving_from_salary = ( annual_salary / 12 ) * portion_saved                        

print( 'Number of months: ', no_of_months )
