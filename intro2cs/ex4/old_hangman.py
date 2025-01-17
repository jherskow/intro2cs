##########################################################################
# FILE : hangman.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex4 2016-2017
# DESCRIPTION:
# A program designed to evaluate how well the humans can spell when human
# lives, umm... , hang.... in the balance.
# (All human lives are of course simulated, but in order to preserve the
# authenticity of the result, this information is never explicitly
# disclosed to the user.
##########################################################################
import hangman_helper as h

ASCII_LOWER_A = 97
INDEX_A = 0
INDEX_Z = 25
ALPHABET_LENGTH = 26
ZERO_INDEX_DIFF = 1


def letter_to_index(letter):
    """ returns 0-indexed i of lowercase letter """
    return ord(letter) - ASCII_LOWER_A


def index_to_letter(number):
    """ returns lowercase letter of 0-indexed i """
    return chr(number + ASCII_LOWER_A)


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    This takes a list of words, and returns a the sub-list of words in the
    list that are:
    The same length as pattern.
    Include no letters from wrong_guess_list.
    If word shares a letter with pattern, it must share all of that letter
    in the same spaces.
    """
    filtered_list = []
    # create list of pattern
    for word in words:
        # set default flag
        match = True
        # create list of letters in word
        if len(word) == len(pattern):
            for (i, letter) in enumerate(pattern):
                if word[i] in wrong_guess_lst:
                    match = False
                    break
                # ensure letter exists in word wherever it is in pattern
                if pattern[i] in word and pattern[i] != word[i]:
                    match = False
                    break
                # if true - ensure letter appears same number of times
                elif pattern[i] != "_" and word.count(pattern[i]) \
                        != pattern.count(pattern[i]):
                    match = False
                    break
                if match and i == len(word) - ZERO_INDEX_DIFF:
                    filtered_list.append(word)
                    break
    return filtered_list


def choose_letter(words, pattern):
    """
    This function returns the most frequent letter from a list of words,
    which is not in the pattern.
    """
    histogram = {}
    for index in range(INDEX_A, ALPHABET_LENGTH):
        histogram[index_to_letter(index)] = 0
    for word in words:
            for letter in word:
                    histogram[letter] += 1
    # create empty list to store the letter and its occurrence number
    max_letter = [0, ""]
    for key in histogram:
        if key in pattern:
            # eliminate this letter as a suggestion
            histogram[key] = 0
        if histogram[key] > max_letter[0]:
            max_letter = [histogram[key], key]
    return max_letter[1]


def update_word_pattern(word, pattern, letter):
    """
    This function takes a word, a hangman pattern, and a letter
    and adds those letters to the pater if and only if they exist in word.
    """
    pattern_list = list(pattern)
    for (i, space) in enumerate(pattern_list):
        if pattern_list[i] == "_" and word[i] == letter:
            pattern_list[i] = letter
    new_pattern = ""
    for (i, space) in enumerate(pattern_list):
        new_pattern += pattern_list[i]
    return new_pattern


def run_single_game(words_list):
    """
    This function runs the game, with any word from the given words_list
    """

    # Initialise game
    word = h.get_random_word(words_list)
    pattern = ""
    error_count = 0
    wrong_guess_lst = []
    won = False
    game_over = False
    for letter in word:
        pattern += "_"
    h.display_state(pattern, error_count, wrong_guess_lst,
                    h.DEFAULT_MSG)
    # get first input
    user_input = list(h.get_input())

    # The Game is ON!!!
    while True:
        # player wants a hint
        if user_input[0] == h.HINT:
            hint = choose_letter(filter_words_list(words_list,
                                 pattern, wrong_guess_lst), pattern)
            h.display_state(pattern, error_count, wrong_guess_lst,
                            h.HINT_MSG + hint)
        # player hazards a guess
        if user_input[0] == h.LETTER and len(user_input[1]) == 1:
            input_letter = user_input[1]
            # check if input is in lowercase
            if INDEX_A <= letter_to_index(input_letter) <= INDEX_Z:
                # check if letter was guessed before
                if input_letter in wrong_guess_lst \
                                            or input_letter in pattern:
                    h.display_state(pattern, error_count,
                                    wrong_guess_lst,
                                    h.ALREADY_CHOSEN_MSG + input_letter)
                # if correct guess of letter in word
                elif input_letter in word:
                    pattern = update_word_pattern(word, pattern,
                                                  input_letter)
                    if pattern == word:
                        won = True
                        game_over = True
                        break
                    h.display_state(pattern, error_count, wrong_guess_lst,
                                    h.DEFAULT_MSG)
                # wrong guess
                else:
                    wrong_guess_lst.append(input_letter)
                    error_count += 1
                    if error_count == h.MAX_ERRORS:
                        game_over = True
                        break
                    h.display_state(pattern, error_count, wrong_guess_lst,
                                    h.DEFAULT_MSG)
            # human error
            else:
                h.display_state(pattern, error_count, wrong_guess_lst,
                                h.NON_VALID_MSG)
        elif game_over is True:
            break
        # wait for next input
        user_input = list(h.get_input())

    if won is True:
        # We've got a WINNER!
        h.display_state(pattern, error_count, wrong_guess_lst,
                        h.WIN_MSG, True)
    else:
        # Pa! They done gone and haaaaanged that man!!
        h.display_state(pattern, error_count, wrong_guess_lst,
                        h.LOSS_MSG + word, True)
    user_input = list(h.get_input())
    # loop until the user makes up their darn mind
    while user_input[0] != h.PLAY_AGAIN:
        user_input = list(h.get_input())
    # run new game if requested, otherwise end.
    if user_input[1] is True:
        run_single_game(words_list)


def main():
    """
    Loads words, and runs game
    """
    words_list = h.load_words()
    run_single_game(words_list)


if __name__ == "__main__":
    h.start_gui_and_call_main(main)
    h.close_gui()
