class Hangman:

  def __init__(self, word_list, num_lives = 5):

    from random import choice

    self.word = choice(word_list)
    self.word_guessed = ['_']*len(self.word)
    #check below line gives correct result
    self.num_letters = len(set(self.word)) - len(set(self.word_guessed)) + 1
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  def print_word(self):

    return f"the word is {self.word}"


  def check_guess(self,guess):

    guess = guess.lower()

    if guess in self.word.lower():
      print(f"Good guess! {guess} is in the word.")

      self.word_guessed = [x[0] if x[0] == guess else x[1] for x in list(zip(self.word.lower(), self.word_guessed))]
      self.num_letters -= 1

    else:
      print(f"Bad luck, {guess} is not in the word")
      self.num_lives -=1
      print (f"you have {self.num_lives} left")


  def ask_for_input(self):

    guess = input('please select a single letter')
    
    while True:

      if len(guess) != 1 or guess.isalpha() == False:
        guess = input("please select a single letter")

      elif guess in self.word_guessed:
        guess = input("please select a letter you haven't already chosen")

      else:

        self.check_guess(guess)
        self.list_of_guesses.append(guess.lower())
        break
