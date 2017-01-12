"""########################################################################
# FILE : wikinetwork.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION: ----
########################################################################"""
# ========== IMPORTS ======================================================
import article

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

    def __init__(self, link_list):
        """
        Initialize a new WikiNetwork.
        :param link_list: A text file in compatible format.
        """
        self._articles = dict()
        self.update_network(link_list)

    def update_network(self, link_list):
        """
        Adds any links or articles not currently in
        the network.
        :param link_list:
        :return:
        """
        for link in link_list:
            for title in link:
                if title not in self._articles:
                    self._articles[title] = article.Article(title)
            if self._articles[link][1] not in self._articles[link][0]:
                self._articles[link][0].\
                        add_neighbor(self._articles[link][1])

    def get_articles(self):
        """
        :return: List of articles in network.
        """
        return list(self._articles.values())

    def get_titles(self):
        """
        :return: List of titles of articles in network
        """
        return list(self._articles.keys())

    def __contains__(self, item):
        """
        :param item: An Article object.
        :return: True if article in network. (by title)
        """
        return item.get_title in self._articles

    def __len__(self):
        """
        :return: Integer size of network.
        """
        return len(self._articles)

    def __repr__(self):
        """
        Returns a string of a dictionary.
        The keys are the articles.
        The values are the articles' strip representation.
        :return: String of dictionary.
        """
        repr_dict = {x: str(self._articles[x]) for x in self._articles}
        return str(repr_dict)

    def __getitem__(self, title):
        """

        :param title:
        :return:
        """
        if title in self._articles:
            return self._articles[title]
        else:
            raise KeyError(title)
