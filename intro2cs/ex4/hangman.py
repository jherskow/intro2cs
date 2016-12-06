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


def display(data):
    """Calls display_state with a dictionary, for readability"""
    h.display_state(data["pattern"], data["error_count"],
                    data["wrong_guess_lst"] , data["msg"],
                    data["ask_play"])
    return None


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

# ===================== GAME SUB-FUNCTIONS ================================


def init_game(words_list):
    """ DOES"""
    # Initialise game
    data = {"word": h.get_random_word(words_list) }
    data["words_list"] = words_list
    data["pattern"] = ""
    data["word_letters"] = list(data["word"])
    data["error_count"] = 0
    data["wrong_guess_lst"] = []
    data["msg"] = h.DEFAULT_MSG
    data["won"] = False
    data["game_over"] = False
    data["ask_play"] = False
    for letter in data["word_letters"]:
        data["pattern"] += "_"
    return data


def game_loop(data):
    """ DOES"""
    while not data["game_over"]:
        display(data)
        data["msg"] = h.DEFAULT_MSG
        # wait for next input
        data["user_input"] = list(h.get_input())
        if data["user_input"][0] == h.HINT:  # the player wants a hint
            data = hint(data)
        # the player hazards a single letter guess
        elif data["user_input"][0] == h.LETTER and \
                len(data["user_input"][1]) == 1:
            data = guess(data)
        else:  # human input error
            data["msg"] = h.NON_VALID_MSG
    return data


def hint(data):
    """ DOES"""
    hint_list = filter_words_list(data["words_list"], data["pattern"],
                                  data["wrong_guess_lst"])
    suggestion = choose_letter(hint_list, data["pattern"])
    data["msg"] = h.HINT_MSG + suggestion
    return data


def guess(data):
    """ DOES"""
    input_letter = data["user_input"][1]
    # check if input is in lowercase
    if INDEX_A <= letter_to_index(input_letter) <= INDEX_Z:
        if input_letter in data["wrong_guess_lst"] \
                or input_letter in data["pattern"]:    # letter was guessed
            data["msg"] = h.ALREADY_CHOSEN_MSG + input_letter
        elif input_letter in data["word"]:             # correct guess
            data["pattern"] = update_word_pattern(data["word"],
                                                  data["pattern"],
                                                  input_letter)
            if data["pattern"] == data["word"]:  # see if guess won game
                data["won"] = True
                data["game_over"] = True
        else:  # wrong guess
            data["wrong_guess_lst"].append(input_letter)
            data["error_count"] += 1
            if data["error_count"] == h.MAX_ERRORS:
                data["game_over"] = True
    else: # invalid input
        data["msg"] = h.NON_VALID_MSG
    return data


def endgame(data):
    """

    :param data:
    :return:
    """
    data["ask_play"] = True
    if data["won"] is True:
        # We've got a WINNER!
        data["msg"] = h.WIN_MSG
    else:
        # Pa! They done gone and haaaaanged that man!!
        data["msg"] = h.LOSS_MSG + data["word"]
    display(data)
    return None

# ===================== GAME MAIN FUNCTION ================================


def run_single_game(words_list):
    """
    This function runs the game, with any word from the given words_list
    """
    data = init_game(words_list)  # setup game
    data = game_loop(data)  # The Game is ON!!!
    endgame(data)  # endgame
    # Play again? - insert coin: 10...9...8...
    user_input = list(h.get_input())
    # loop until the user makes up their damn mind
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
