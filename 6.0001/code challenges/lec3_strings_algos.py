# ORIGINAL CODE BY ANA BELL

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
   char = word[i]
   if char in an_letters:
       print("Give me an " + char + "! " + char)
   else:
       print("Give me a  " + char + "! " + char)
   i += 1
print("What does that spell?")
for i in range(times):
   print(word, "!!!")


    
# CHALLENGE: rewrite while loop with a for loop

# SOLUTION
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for char in word:
   if char in an_letters:
       print("Give me an " + char + "! " + char)
   else:
       print("Give me a  " + char + "! " + char)
print("What does that spell?")
for i in range(times):
   print(word, "!!!")

