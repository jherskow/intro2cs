##########################################################################
# FILE : hangman.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex4 2016-2017
# DESCRIPTION: #todo
##########################################################################
import hangman_helper as h

ASCII_LOWER_A = 97
ALPHABET_LEN = 25

def letter_to_index(letter):
    """ returns 0-indexed i of lowercase letter """
    return ord(letter) - ASCII_LOWER_A


def index_to_index(number):
    """ returns lowercase letter of 0-indexed i """
    return chr(number + ASCII_LOWER_A)


def update_word_pattern(word, pattern, letter): #todo docstring
    """
    This function
    :param word:
    :param pattern:
    :param letter:
    :return:
    """
    word_list = list(word)
    pattern_list = list(pattern)
    for (i, space) in enumerate(pattern_list):
        if pattern_list[i] == "_" and word_list[i] == letter:
            pattern_list[i] = letter
    new_pattern = ""
    for (i, space) in enumerate(pattern_list):
        new_pattern += pattern_list[i]
    return new_pattern


def run_single_game(words_list): #todo
    """

    :param words_list:
    :return:
    """
    # Initialise game
    word = h.get_random_word(words_list)
    pattern = ""
    word_letters = list(word)
    error_count = 0
    wrong_guess_lst = []
    for letter in word_letters:
        pattern += "_"
    h.display_state(pattern, error_count, wrong_guess_lst,
                                 h.DEFAULT_MSG)

    # The Game is ON!!!
    game_over = False
    while not game_over:
        h.display_state(pattern, error_count, wrong_guess_lst, h.DEFAULT_MSG)
        pattern_list = list(pattern)
        user_input = h.get_input()
        input_index = letter_to_index(user_input)
        if user_input.isalpha() and len(user_input) == 1 \
                                and input_index <= ALPHABET_LEN:
            if user_input in wrong_guess_lst or user_input in pattern_list:
                h.display_state(pattern, error_count,
                                wrong_guess_lst,
                                h.ALREADY_CHOSEN_MSG + user_input)
            elif user_input in word_letters:
                update_word_pattern(word, pattern, user_input)
            else:
                wrong_guess_lst += 1
        else:
            h.display_state(pattern, error_count, wrong_guess_lst,
                            h.NON_VALID_MSG)
        if wrong_guess_lst > h.MAX_ERRORS:
            game_over = True
            won = False
        elif pattern == word:
            game_over = True
            won = True
    if won == True:
        h.display_state(pattern, error_count, wrong_guess_lst, h.WIN_MSG, True)
    else:
        h.display_state(pattern, error_count, wrong_guess_lst, h.LOSS_MSG, True)



def main(): #todo
    """

    :return:
    """
    words_list = h.load_words()
    run_single_game(words_list)


if __name__ == "__main__":
    h.start_gui_and_call_main(main)
    h.close_gui()

