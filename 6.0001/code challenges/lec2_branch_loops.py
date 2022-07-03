# Original Code by Ana Belle
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
   n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")



# PROBLEM

# Try expanding this code to show a sad face if you go right twice and flip the table any more times than that.
# Hint: use a counter

 
   
# SOLUTION(Incomplete as of yet, throws an infinte loop)

# SIMPLE PROBLEM DESCRIPTION
# right<=2, show happy face
# right=3, show sad face
# right>3, flip table

user_input = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while user_input == "right" or user_input == "Right":

   counter=1
   while user_input == "right" or user_input == "Right":
      user_input+=counter
   print(counter)

   if counter<=2:
      user_input= input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")      #happy
   elif counter==3:
      user_input= input("You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? ")      #sad
   elif counter>3:
      user_input= input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right?")      #flipping table

print("\nYou got out of the Lost Forest!\n\o/")
