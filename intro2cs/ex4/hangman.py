##########################################################################
# FILE : hangman.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex4 2016-2017
# DESCRIPTION:
##########################################################################
import hangman_helper


def update_word_pattern(word, pattern, letter):
    word_length = len(word)
    word_list = word.split()
    pattern_list = pattern.split()
    for space in pattern_list:
        if pattern_list[space] == "_" and word_list[space] == letter:
            pattern_list[space] = letter
    new_pattern = ""
    for space in pattern_list:
        new_pattern += pattern_list[space]
    return new_pattern




def run_single_game(words_list):
    words_list = 1 #todo


