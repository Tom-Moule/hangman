word_list = ["apple", "banana", "raspberry", "grape", "mango"]
#print(word_list)

import random
word = random.choice(word_list)
#print(word)


#the below makes sure final user input is a single alphabetic character
def validate_input(user_input):

  while True:

    if len(user_input) == 1 and user_input.isalpha():

      #print ("Good Guess")
      break

    else:

      user_input = input("Invalid letter. Please, enter a single alphabetical character.")

  return user_input


#the below function checks whether user inputted character is in the hidden word
def check_input(user_input):

  user_input = user_input.lower()

  
  if user_input in word.lower():

    print (f"good news! {user_input} is in the word.")

  else:

    print (f"Sorry, {user_input} is not in the word. Try again.")


#below function asks for input, validates it, and checks whether it is in hidden word
def get_input_validate_and_check():
  user_input = input("select a single letter")
  validated_input = validate_input(user_input)
  check_input(validated_input)


get_input_validate_and_check()
