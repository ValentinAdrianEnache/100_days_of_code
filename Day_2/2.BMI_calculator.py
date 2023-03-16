"""Exercise 2 - BMI Calculator"""

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_as_int = float(height)
weight_as_int = int(weight)
result = int(weight_as_int / height_as_int ** 2)
print(result)
