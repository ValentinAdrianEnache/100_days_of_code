"""Exercise 3 - Adding Even Numbers"""

# Instructions
# You are going to write a program that calculates the sum
# of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100:
#
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#
# Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation

# Solution 1:
even_sum = 0
for even_number in range(2, 101, 2):
    even_sum += even_number
print(even_sum)

# Solution 2:
# even_sum = 0
# for even_number in range(1, 101):
#     if even_number % 2 == 0:
#         even_sum += even_number
# print(even_sum)
