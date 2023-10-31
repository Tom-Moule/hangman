word_list = ["apple", "banana", "raspberry", "grape", "mango"]

print(word_list)

import random

word = random.choice(word_list)

print(word)

user_letter_guess = input("select a single letter")

if len(user_letter_guess) == 1 and user_letter_guess.isalpha():

  print ("Good Guess")

else:

  print("Oops! That is not a valid input.")




