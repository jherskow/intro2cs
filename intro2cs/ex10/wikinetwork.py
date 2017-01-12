"""########################################################################
# FILE : wikinetwork.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION: ----
########################################################################"""
# ========== IMPORTS ======================================================

# ========== FUNCTIONS ============================================


def read_article_links(filename):
    """
    Converts text file of compatible format into
    a list of article-pair tuples.
    :param filename: text file of compatible format
    :return: list of (article,pair) tuples
    """
    pairs = []
    with open(filename, 'r') as f:
        line = f.readline()
        pair = line.split('\t')
        pair_tup = tuple(pair)
        pairs.append(pair_tup)
    return pairs

# ========== CLASS WIKINETWORK ============================================


class WikiNetwork:
    """
    A class representing ---.
    """
    # ===== WikiNetwork - class constants =====

    # ===== WikiNetwork - class methods =======

    def __init__(self):
        """
        Initialize a new WikiNetwork.
        """
