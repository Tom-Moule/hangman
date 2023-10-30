word_list = ["apple", "banana", "raspberry", "grape", "mango"]

print(word_list)

import random

word = random.choice(word_list)

print(word)

user_letter_guess = input("select a single letter")

if len(guess) == 1 and guess.isalpha():

  print ("Good Guess")

else:

  print("Oops! That is not a valid input.")




