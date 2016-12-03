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
    pattern_list = list(pattern)
    for word in words:         #todo needs work!!!
        match = True
        word_letters = list(word)
        if len(word_letters) == len (pattern):
            for (i, letter) in enumerate(pattern_list):
                if word_letters[i] in wrong_guess_lst:
                    match == False
                    break
                if word_letters[i] == pattern_list[i]:
                    for letter in word_letters:
                        if letter == word_letters[i] \
                                and letter in pattern_list[i]:
                            match = False
                            break
                if match == False:
                    break
        filtered_list.append(word)
    return filtered_list


def choose_letter(words, pattern):
    """

    :param words:
    :param pattern:
    :return:
    """
    histogram = []
    for i in range(INDEX_A, INDEX_Z):
        histogram.append(0)
    for word in words:
        word_letters = list(word)
        for i in range(INDEX_A, INDEX_Z):
            for letter in word_letters:
                if letter_to_index(letter) == i:
                    histogram[i] +=1
    max_letter = max(histogram)
    for i in range(INDEX_A, INDEX_Z):
        if histogram[i] == max_letter:
            return index_to_letter(i)
    return None


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
            filtered_list = filter_words_list(words_list, pattern,
                                              wrong_guess_lst)
            hint = choose_letter(filtered_list, pattern)
            h.display_state(pattern, error_count, wrong_guess_lst,
                            h.HINT_MSG + hint)
        # player hazards a guess
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


def main(): #todo
    """

    :return:
    """
    words_list = h.load_words()
    run_single_game(words_list)


if __name__ == "__main__":
    h.start_gui_and_call_main(main)
    h.close_gui()

