# Write a program to check a character is in vowel or not. 
# Declare a global variable vow = “aeiouAEIOU”
def is_vowel(char):
    # Define a string of vowels
    vowels = 'aeiouAEIOU'
    # Check if the character is in the string of vowels
    return char in vowels

# Get user inputi
character = input("Enter a character: ")

# Ensure the input is a single character
if len(character) == 1 and character.isalpha():
    if is_vowel(character):
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is not a vowel.")
else:
    print("Please enter a single alphabetic character.")
