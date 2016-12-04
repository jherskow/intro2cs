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
ALPHABET_LENGTH = 26


def letter_to_index(letter):
    """ returns 0-indexed i of lowercase letter """
    return ord(letter) - ASCII_LOWER_A


def index_to_letter(number):
    """ returns lowercase letter of 0-indexed i """
    return chr(number + ASCII_LOWER_A)


def filter_words_list(words, pattern, wrong_guess_lst):
    """

    :param words:
    :param pattern:
    :param wrong_guess_lst:
    :return:
    """
    filtered_list = []
    # create list of pattern
    for word in words:       # todo not filtering words with wrong guess!!
        # set default flag
        match = True
        # create list of letters in word
        if len(word) == len(pattern):
            for (i, letter) in enumerate(pattern):
                if word[i] in wrong_guess_lst:
                    match = False
                    break
                if word[i] == pattern[i]:
                    # ensure letter exists in all spaces
                    for letter in word:
                        if letter == word[i] \
                                and letter in pattern[i]:
                            # invalidate and skip to next word
                            match = False
                            break
        if not match:
            break
        filtered_list.append(word)
    return filtered_list


def choose_letter(words, pattern):
    """

    :param words:
    :param pattern:
    :return:
    """
    histogram = {}
    for index in range (INDEX_A, ALPHABET_LENGTH):
        histogram[index_to_letter(index)] = 0
    for word in words:
            for letter in word:
                    histogram[letter] += 1
    max_letter = [0,""]
    for key in histogram:
        if key in pattern:
            # eliminate this letter as a suggestion
            histogram[key] = 0
        if histogram[key] > max_letter[0]:
            max_letter = [histogram[key], key]
    return max_letter[1]


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
    while True:
        h.display_state(pattern, error_count, wrong_guess_lst, h.DEFAULT_MSG)
        # refresh the list of letters currently in the pattern
        pattern_list = list(pattern)
        # player wants a hint
        if user_input[0] == h.HINT:
            hint = choose_letter(filter_words_list(words_list,
                                 pattern, wrong_guess_lst), pattern)
            h.display_state(pattern, error_count, wrong_guess_lst,
                            h.HINT_MSG + hint)
        # player hazards a guess # todo consider making "guess" function
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
                # if correct guess of letter in word
                elif input_letter in word_letters:
                    pattern = update_word_pattern(word, pattern, input_letter)
                    h.display_state(pattern, error_count, wrong_guess_lst,
                                    h.DEFAULT_MSG)
                # wrong guess
                else:
                    wrong_guess_lst.append(input_letter)
                    error_count += 1
                    h.display_state(pattern, error_count, wrong_guess_lst,
                                    h.DEFAULT_MSG)
            # human error
            else:
                h.display_state(pattern, error_count, wrong_guess_lst,
                                h.NON_VALID_MSG)
        # check for win\loss conditions
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


def main():
    """

    :return:
    """
    words_list = h.load_words()
    run_single_game(words_list)


if __name__ == "__main__":
    h.start_gui_and_call_main(main)
    h.close_gui()

# todo comprehensive commenting, docstrings, and description in header
# todo fix hint issue
# todo remove all list-making of strings!!!