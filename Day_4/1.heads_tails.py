"""Exercise 1 - Heads or Tails"""
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

number = random.randint(0, 1)
heads = 'Heads'
tails = 'Tails'
if number:
    print(tails)
else:
    print(heads)


