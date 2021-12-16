# review

# palidrome

# word = input ("Enter word: ")

#here we're indexing at zero and storing the lengh of the word in an array
#for index in range(0, len(word)):
    #print(word[index])

# reversed_word = ""

# # we can reverse the order as well
# for index in range(0, len(word)):
#     # here. the += is adding the characters to the stored reversed word, one char at a time. it will print them all on individual lines, eventually the entire word on one line
#     reversed_word += word[(len(word)-1) -index]
#     print(f"{reversed_word}")

# if word == reversed_word:
#     print("Palidrome")
# else:
#     print("NOT PALIDROM")

# print(reversed_word)

# we can write all this as a function as well

word = input ("Enter word: ")

def find_palidrome(word):
    reversed_word = ""
    for index in range(0, len(word)):
        reversed_word += word[(len(word)-1) -index]
        print(f"{reversed_word}")
        
    if word == reversed_word:
        print("Palidrome")
    else:
        print("NOT PALIDROM")

find_palidrome(word)