##########################################################################
# FILE : hangman.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex4 2016-2017
# DESCRIPTION: #todo
##########################################################################
import hangman_helper as h

ASCII_LOWER_A = 97
INDEX_A = 0
INDEX_Z = 25


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


def run_single_game(words_list):  #todo
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
    # get first input
    user_input = list(h.get_input())

    # The Game is ON!!!
    game_over = False
    while True:
        h.display_state(pattern, error_count, wrong_guess_lst, h.DEFAULT_MSG)
        # refresh the list of letters currently in the pattern
        pattern_list = list(pattern)
        if user_input[0] == h.LETTER and len(user_input[1]) == 1 :
            input_letter = user_input[1]
            # check if input is in lowercase
            if INDEX_A <= letter_to_index(input_letter) <= INDEX_Z:
                # check if letter was guessed before
                if input_letter in wrong_guess_lst \
                                            or input_letter in pattern_list:
                    h.display_state(pattern, error_count,
                                    wrong_guess_lst,
                                    h.ALREADY_CHOSEN_MSG + input_letter)
                elif input_letter in word_letters:
                    pattern = update_word_pattern(word, pattern, input_letter)
                    h.display_state(pattern, error_count, wrong_guess_lst,
                                    h.DEFAULT_MSG)
                else:
                    wrong_guess_lst.append(input_letter)
                    error_count += 1
                    h.display_state(pattern, error_count, wrong_guess_lst,
                                    h.DEFAULT_MSG)
            else:
                h.display_state(pattern, error_count, wrong_guess_lst,
                                h.NON_VALID_MSG)
        if error_count == h.MAX_ERRORS:
            won = False
            break
        elif pattern == word:
            won = True
            break
        # wait for next input
        user_input = list(h.get_input())

    if won == True:
        # We've got a WINNER!
        h.display_state(pattern, error_count, wrong_guess_lst,
                        h.WIN_MSG, True)
    else:
        # Another man done gone, another maaaaan done gone, another man done...
        h.display_state(pattern, error_count, wrong_guess_lst,
                        h.LOSS_MSG + word, True)
    user_input = list(h.get_input())
    while user_input[0] != h.PLAY_AGAIN:
        user_input = list(h.get_input())
    if user_input[1] == True:
        run_single_game(words_list)


def main(): #todo
    """

    :return:
    """
    words_list = h.load_words()
    run_single_game(words_list)


if __name__ == "__main__":
    h.start_gui_and_call_main(main)
    h.close_gui()

