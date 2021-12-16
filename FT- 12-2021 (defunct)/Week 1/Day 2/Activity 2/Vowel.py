print("This program checks if your single letter input is a vowel")

vowels = ['a', 'e', 'i', 'o','u', 'y']
user_input = input("Please input a single letter: ").lower()

def is_vowel():
    if user_input[0] in vowels:
        print("Your input is a vowel!")
    else:
        print("Your input is not a vowel!")

is_vowel()


