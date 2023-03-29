"""Caesar Cipher"""

import string
from art import logo
print(logo)

# # using string for filling alphabets
# alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)
# direction = input("Type 'encode' to encript, type 'decode' to decrypt:\n")
# text = input("Type your message: \n").lower()
# shift = int(input("Type the shift number: \n"))


# solution 1
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")
#
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)

# solution 2

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'decode':
            shift_amount = abs(shift_amount) *-1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


should_continue = True
while should_continue:
    # using string for filling alphabets
    alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)
    direction = input("Type 'encode' to encript, type 'decode' to decrypt:\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift %= 26 
    print(shift)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye!")
