"""Exercise 2 - BMI 2.0"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)

standard = 'Your BMI is'
underweight = 'you are underweight.'
normal = 'you have a normal weight.'
slightly = 'you are slightly overweight.'
obese = 'you are obese.'
c_obese = 'you are clinically obese.'
if bmi < 18.5:
    print(f'{standard} {bmi}, {underweight}')
elif bmi < 25:
    print(f'{standard} {bmi}, {normal}')
elif bmi < 30:
    print(f'{standard} {bmi}, {slightly}')
elif bmi < 35:
    print(f'{standard} {bmi}, {obese}')
else:
    print(f'{standard} {bmi}, {c_obese}')
