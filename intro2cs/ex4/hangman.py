##########################################################################
# FILE : hangman.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex4 2016-2017
# DESCRIPTION:
##########################################################################
import hangman_helper


def update_word_pattern(word, pattern, letter):
    """

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


def run_single_game(words_list):
    """

    :param words_list:
    :return:
    """
    # get random word (helper)
    # init pattern, leterrs, bad guesses
    print(DEFAULT_MESSAGE)

    end = False
    while not end:
        """""
        display state (helper)
        get input of guess
        if input is guess:
            if not valid (single lowercase letter)
                NON_VALID_MSG
            else if already chose
                ALREADY_CHOSE_MSG
            else if in word
                update word update_word_pattern
                DEFAULT_MSG
            else
                update bad guess
                DEFAULT_MSG


    display_state()
    LOSS_MSG or WIN_MSG
    (add the word itslef)
    ask_play=TRUE
        """
def main():
    """

    :return:
    """
    """
    loads words

    runs single game
    ask play again
    """
