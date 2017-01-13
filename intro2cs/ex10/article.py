"""########################################################################
# FILE : article.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION: ----
########################################################################"""
# ========== IMPORTS ======================================================
import copy as c

# ========== CLASS ARTICLE ================================================


class Article:
    """
    A class representing ---.
    """
    # ===== Article - class constants =====

    # ===== Article - class methods =======

    def __init__(self, article_title):
        """
        Initialize a new Article.
        """
        self._title = article_title
        self._neighbors = dict()
        self._neighbors_list = []

    def get_title(self):
        """
        Returns the Article's own title.
        :return: String of title.
        """
        return self._title

    def add_neighbor(self, neighbor):
        """
        Adds an Article to neighbors dict.
        :param neighbor: Obj of type Article
        """
        if neighbor not in self:
            self._neighbors[neighbor.get_title()] = neighbor
            self._neighbors_list.append(neighbor.get_title())

    def get_neighbors(self):
        """
        :return: List of neighboring articles.
        """
        return self._neighbors_list

    def __repr__(self):
        """
        :return: String of tuple (title, neighbor_list)
        """
        title = self._title
        neighbor_list = self._neighbors_list
        repr_tup = (title, neighbor_list)
        return str(repr_tup)

    def __len__(self):
        """
        :return: Integer size of neighbors dict.
        """
        return len(self._neighbors)

    def __contains__(self, item):
        """
        :return: True if article is in neighbors dict. (by title)
        """
        return item.get_title in self._neighbors
