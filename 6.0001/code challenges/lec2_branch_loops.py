# ORIGINAL CODE BY ANA BELL

n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
   n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")



# CHALLENGE: Try expanding this code to show a sad face if you go right twice and flip the table any more times than that.
# HINT: use a counter 

 
   
# SOLUTION(Incomplete as of yet)

# SIMPLE PROBLEM DESCRIPTION
# right<=2, show happy face
# right=3, show sad face
# right>3, flip table

# SIMPLE PROBLEM DESCRIPTION
# right<=2, show happy face
# right=3, show sad face
# right>3, flip table

# Taking user input
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")

counter = 0
 
while n == 'right':
    counter += 1
    
    if counter < 3:
        print('You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ')
    elif counter == 3:
        print('You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? ')
    else:
        print('You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ')
        break
    
print("\nYou got out of the Lost Forest!\n\o/")
