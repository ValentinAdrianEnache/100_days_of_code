"""Debug Leap Year"""

# year = input("Which year do yo want to check")
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Not leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


year = int(input("Which year do yo want to check"))  # it was a str not an int

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Not leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
