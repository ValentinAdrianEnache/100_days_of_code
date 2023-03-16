"""Exercise 5 - Love Calculator"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lower_names = name1.lower() + name2.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = first_digit * 10 + second_digit
# love_score = int(str(true) + str(love))


if (10 > score) or (score > 90):
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
