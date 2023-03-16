"""Exercise 3 - Life in Weeks
1 year = 365 days
1 year = 52 weeks
1 year = 12 months
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = 12 * years_remaining
print(f"You have {days_remaining} days, {weeks_remaining}"
      f" weeks, and {months_remaining} months left.")


