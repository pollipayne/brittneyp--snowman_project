  
SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
MAX_WRONG_GUESSES = 7
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
  '*   *   *  ',
  ' *   _ *   ',
  '   _[_]_ * ',
  '  * (")    ',
  '  \( : )/ *',
  '* (_ : _)  ',
  '-----------'
  ]

def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 'Sorry, you lose!  The word was {snowman_word}' if the player loses
    """
    word_list = build_word_list(snowman_word)
    correct_guesses = []
    wrong_guesses = []
    while len(wrong_guesses) < SNOWMAN_MAX_WRONG_GUESSES and len(correct_guesses) <= len(snowman_word):
      guess = get_letter_from_user(wrong_guesses, correct_guesses)
      all_guesses = update_and_check_word_list(word_list, guess)
      print_word_list(word_list)
      if guess in snowman_word:
        print("Letter found.")
        correct_guesses.append(guess)
      else:
        print(f"The letter {guess} is not in the word.")
        wrong_guesses.append(guess)
      print_snowman_graphic(len(wrong_guesses))
      if all_guesses == True:
        print("Congratulation, you win!")
        break
      elif len(wrong_guesses) >= SNOWMAN_MAX_WRONG_GUESSES:
        print(f"Sorry, you lose!  The word was {snowman_word}")



# 
def print_snowman_graphic(num_wrong_guesses):
    """This function prints a portion of the 
    snowman depending on the number of 
    wrong guesses
    """
    for num in range(0, num_wrong_guesses):
        print(SNOWMAN_GRAPHIC[num])


def build_word_list(word):
    """This function builds a list of dictionaries
    With each letter and "guessed": False
    Example: [ { 'letter': 'a', 'guessed': False }, 'letter': 'b', 'guessed': False }, ]
    """
    word_list = []
    for letter in word:
        letter_dict = {"letter": letter, "guessed": False}
        word_list.append(letter_dict)
    return word_list

def print_word_list(word_list):
    """This function prints the letters of the word
    based on if that letter has been guessed or not
    """

    output_string = ""
    for elem in word_list:
        if elem["guessed"]:
            output_string += elem["letter"]
        else:
            output_string += "_"
        output_string += " "
    print(output_string)


def get_letter_from_user(wrong_list, correct_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        # NEW SECTION
        elif user_input_string in wrong_list or user_input_string in correct_guesses_list:
            print("You have already guessed that letter!")
        # END NEW SECTION
        else:
            valid_input = True

    return user_input_string

def update_and_check_word_list(list_of_letters, guessed_letter):
    all_letters_guessed = True
    for letter_dict in list_of_letters:
        if (guessed_letter == letter_dict["letter"]):
            letter_dict["guessed"] = True
        elif (not letter_dict["guessed"]):
            all_letters_guessed = False
    
    return all_letters_guessed
