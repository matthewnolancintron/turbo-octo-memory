# Write your code here
from random import choice

print("H A N G M A N\n")

list_of_words = ['python', 'java', 'kotlin', 'javascript']
the_word = choice(list_of_words)

"""
hint = ''
for index, character in enumerate(the_word):
    if index <= 2:
        hint += character
    else:
        hint += '-'
# test hint
# print(hint)

user_guess = input("Guess the word {hint}: ".format(hint=hint))
"""
starting_hint = ''
for index, character in enumerate(the_word):
    starting_hint += '-'



num_letter_to_guess = len(the_word)
num_tries = 8
user_attempts = 0
itter_count = 0
hint = []
# rename later : hold correct user guesses
user_letters_guess_list = []
# rename later: hold incorrect user guess
all_guess = []
is_guess_complete = False
exit_message = "Thanks for playing\nWe'll see how well you did in the next stage"
start_game = False
is_deciding_to_play = True
# menu
while is_deciding_to_play:
  player_decision_to_play = input("Type \"play\" to play the game,\"exit\" to quit:")
  if player_decision_to_play == 'play':
    # set start game bool to true to activate the game loop
    start_game = True
    # set is_deciding_to_play to false, to exit the start game menu
    is_deciding_to_play = False
  elif player_decision_to_play == 'exit':
    # don't start the game, but do exit the game menu
    is_deciding_to_play = False
  else:
    # gave an answer other than the two options re-prompt question
    continue


# game loop
while user_attempts < num_tries and start_game:
  #print("value of user_attemps", user_attempts)
  # check if user guess is complete
  # num check will be used to count the number correct guess
  # being currently made
  num_check = 0
  for letter in the_word:
      if letter in user_letters_guess_list:
          num_check += 1

  # when num check is equal to the length of the word
  if num_check == len(the_word):
    # set ... to true
    is_guess_complete = True

  # reset num_letter_to_guess to redo the calc or
  # else the result will go into negative
  num_letter_to_guess = len(the_word)
  for index, letter in enumerate(user_letters_guess_list):
    if letter in the_word:
      num_letter_to_guess -= 1
      # print("is_guess_complete value: ", is_guess_complete)
      # print("num_letter_to_guess: ", num_letter_to_guess)

    if num_letter_to_guess == 0:
      # print("num_letter_to_guess: ", num_letter_to_guess)
      # print("is_guess_complete value: ", is_guess_complete)
      is_guess_complete = True

  if is_guess_complete:
    user_attempts += 1
  else:
    # handle user input loop
    # print the guess
    try: hint_string
    except NameError:
      print(starting_hint)
    else:
      print(hint_string.strip())

    # ask for input
    user_letter_guess = input("Input a letter:").rstrip()
    if len(user_letter_guess) != 1 or not(user_letter_guess.isalpha() and user_letter_guess.islower()):
        # enter the correct message based on the wrong formatting
        if len(user_letter_guess) != 1:
            print("You should input a single letter")
        if not(user_letter_guess.isalpha() and user_letter_guess.islower()):
            print("Please enter a lowercase English letter")

        if not(is_guess_complete) and user_attempts != 8:
            print()
            # print("a")
        # start the game loop over input is not right
        continue
    else:
      # print("passed checking input, starting game")
      # input is good, continue with the game loop
      # check if the letter has already been guessed
      if user_letter_guess in user_letters_guess_list or user_letter_guess in all_guess:
        print("You've already guessed this letter")
        if not(is_guess_complete) and user_attempts != 8:
          print()
          #print('b')
        # restart input, letter's already been guessed
        # print()
        continue

      # letter has not been guessed yet, continue the game
      # for format create a newline between input and guess
      """
      need to count the occurnes of the user_letter_guess
      in the_word and add it to the 
      user_letters_guess_list that many times
      should be able to use .count method for that.
      """
      for num_adds in range(the_word.count(user_letter_guess)):
        user_letters_guess_list.append(user_letter_guess)
        # print(user_letters_guess_list)
        # test it
      else:
        # if it doesn't show up in the word then add it to
        all_guess.append(user_letter_guess)

      if user_letter_guess in the_word:
        # print("letter is in the word")
        if not(is_guess_complete) and user_attempts != 8:
          # hint
          try: hint_string
          except NameError:
            print()
          else:
            """
            count number of blanks left in hint
            hint_string.count('-')
            count the number of time the user_guess_letter
            shows up in the word
            the_word.count(user.guess_letter)
            
            if they are equal then it's the final correct guess
            so don't print the empty line
            """
            if hint_string.count('-') != the_word.count(user_letter_guess):
                print()
          #print('c')
        # create hint
        if len(hint) == 0:
          # print("len hint is", len(hint))
          for index, character in enumerate(the_word):
            if user_letter_guess == character:
              hint.append(character)
            else:
              hint.append('-')
        else:
          for word_index, word_letter in enumerate(the_word):
            if user_letter_guess == word_letter:
              # hint.insert(word_index, user_letter_guess)
              hint[word_index] = user_letter_guess
              # print(hint)

        hint_string = ''
        for letter in hint:
          hint_string += letter

        # check hint string
        # print(hint_string)
      else:
        print("That letter doesn't appear in the word")
        user_attempts += 1
        if not(is_guess_complete) and user_attempts != 8:
          #print(user_attempts)
          print()
          # print('d')
    # print()
else:
    if player_decision_to_play == 'play':
      # print("is_guess_complete value: ", is_guess_complete)
      print(f"You guessed the word {the_word}!\nYou survived!" if is_guess_complete == True else "You lost!")
