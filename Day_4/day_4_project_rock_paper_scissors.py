"""Day 4 Project: Rock Paper Scissors"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random
boot_score = 0
user_score = 0
boot_choice = random.choice([rock, scissors, paper])

user_choice = str.lower(input("Enter your choice:\n 'R' from rock;\n 'S' from scissors;\n 'P' from paper\n"))
if user_choice == 'r':
    user_choice = rock
elif user_choice == 's':
    user_choice = scissors
elif user_choice == 'p':
    user_choice = paper
choices = (rock, scissors, paper)
user_win = 'Congratulations, You win!'
boot_win = 'You lose! Try again!'
print(f'Thanks, your choice is: {user_choice}')
print(f'boot choice was: {boot_choice}')
if boot_choice == user_choice:
    print('It is a draw, Try again!')
elif user_choice not in choices:
    print('You typed an invalid letter! You lose!')
else:
    if boot_choice == rock and user_choice == scissors:
        print(user_win)
        user_score += 1
    elif boot_choice == paper and user_choice == scissors:
        print(user_win)
        user_score += 1
    elif boot_choice == scissors and user_choice == rock:
        print(user_win)
        user_score += 1
    else:
        print(boot_win)
        boot_score += 1
    print(f'score is: you = {user_score} : boot = {boot_score}')
