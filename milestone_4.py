class Hangman:

 """
  A class to represent words to be guessed by a user, and track successes of user guesses
  
  
  Attributes
  ----------

  __word: str 
      private attribute that represents the word that needs to be guessed
  word_guessed: str
      represents the letters a user has correctly guessed so far
  num_letters: int
      represents the number of unique letters left to guess
  num_lives: int
      represents the number of lives the user has left
  __word_list: str
      private attribute that represents the possible words the words to guess could have been chosen from
  list_of_guesses: str
      represents the letters a user has already guessed

  Methods
  -------

  check_guess:
       Checks whether the letter guessed by the user is in the word. 
       Updates attributes accordingly.
  ask_for_input_and_check:
       Asks users for input, validates input, and runs check_guess, to establish
       if the user's chosen letter is in the word.
  

  """


  def __init__(self, word_list, num_lives = 5):


  """
    Constructs all attributes needed for instances of the hangman, class.

        Parameters
        ----------
            word_list : str
                list of words that could be chosen as word to be guessed
            num_lives : int
                the number of times a user can make an incorrect guess before
                losing. Default value = 5.

   """

    from random import choice

    self.word = choice(word_list)
    self.word_guessed = ['_']*len(self.word)
    self.num_letters = len(set(self.word)) - len(set(self.word_guessed)) + 1
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  def print_word(self):

    return f"the word is {self.word}"


  def check_guess(self,guess):

  """
   Checks whether the letter guessed by a user was in the word.

   If the letter is in the word, a message of success is printed to the user and 
   the word.guessed attribute is updated to reveal where the correctly guessed 
   letter appears in the word. The num.letters attribute is also decreased by one.

   If the letter is NOT in the word, a message of failture is printed to the user,
   and the num_lives attribute is decreased by one.


   Parameters
   ----------

   self

   guess: str
        content inputted by user - asked for within
        method, 'ask_for_intro_and_check'
        

   Returns
   -------

    if guessed letter is in the hidden word, word_guessed updates,
    and num_letters decreases by 1. A message of success is also printed
    to the user.

    if guessed letter is not in the hidden word, the num_lives attribute 
    decreases by one; and a message of failure is printed to the user.      

    """



    guess = guess.lower()

    if guess in self.word.lower():
      print(f"Good guess! {guess} is in the word.")

      self.word_guessed = [x[0] if x[0] == guess else x[1] for x in list(zip(self.word.lower(), self.word_guessed))]
      self.num_letters -= 1

    else:
      print(f"Bad luck, {guess} is not in the word")
      self.num_lives -=1
      print (f"you have {self.num_lives} lives  left")


  def ask_for_input_and_check(self):
 
  """
   aks users to input a letter, and validates that their input is indeed a letter,
   asking them repeatedly until they return a letter.

   when letter is inputted, the method calls the check_guess method, and updates
   the list_of_guesses parameter, to reflect the newly guessed letter.


   Parameters
   ----------

   self

  
   Returns
   -------
   Calls check_guess (see above for details), and updates list_of_guesses attribute
        

    """


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
