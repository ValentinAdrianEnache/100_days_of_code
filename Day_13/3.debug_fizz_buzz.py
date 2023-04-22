"""Debug FizzBuzz"""

# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: #"and" not "or"
        print("FizzBuzz")
    elif number % 3 == 0: #"elif" not "if"
        print("Fizz")
    elif number % 5 == 0: #"elif" not "if"
        print("Buzz")
    else:
        print(number)  #just (number) not ([number])
