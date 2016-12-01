##########################################################################
# FILE : hangman.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex4 2016-2017
# DESCRIPTION: #todo
##########################################################################
import hangman_helper

ASCII_LOWER_A= 97
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
    word = hangman_helper.get_random_word() #todo

    #def update_data(self, pattern, err_cnt, wrong_guess_lst, msg,
                    #ask_play):
    # init pattern, leterrs, bad guesses
   # hangman_helper.update_data(self, pattern, 0, wrong_guess_lst, msg,
                   # ask_play)

    game_over = False
    while not game_over:
        """""
        display state (helper)
        input = get_input()
        if not valid
            NON_VALID_MSG
        if ASCII_LOWER_A <= letter_to_index(input) <= ALPHABET_LEN
            if already chose
                ALREADY_CHOSE_MSG
            else if in word_list
                update_word_pattern(word, pattern, letter)
                DEFAULT_MSG
            else
                update bad guess
                DEFAULT_MSG


    display_state()
    LOSS_MSG or WIN_MSG
    (add the word itself)
    ask_play=TRUE
        """


def main(): #todo
    """

    :return:
    """
    hangman_helper.load_words()

    if __name__ == "__main__":
        hangman_helper.start_gui_and_call_main(main)
        hangman_helper.close_gui()

    #ask play again #todo

