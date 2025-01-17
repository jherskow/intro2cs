"""########################################################################
# FILE : article.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION: Implements article object and functionality.
########################################################################"""
# ========== IMPORTS ======================================================
import copy

# ========== CLASS ARTICLE ================================================


class Article:
    """
    A class representing an article, with a title and a list of
    neighboring articles that are linked to by the article.
    """

    # ===== Article - class methods =======

    def __init__(self, article_title):
        """
        Initialize a new Article.
        """
        self._title = article_title
        self._neighbors = dict()

    def get_title(self):
        """
        Returns the Article's own title.
        :return: String of title.
        """
        return copy.copy(self._title)

    def add_neighbor(self, neighbor):
        """
        Adds an Article to neighbors dict.
        :param neighbor: Obj of type Article
        """
        if neighbor not in self:
            self._neighbors[neighbor.get_title()] = neighbor

    def get_neighbors(self):
        """
        :return: List of neighboring articles.
        """
        return [art_obj for art_obj in self._neighbors.values()]

    def __repr__(self):
        """
        :return: String of tuple (title, neighbor_list)
        """
        title = self._title
        neighbor_list = [art_title for art_title in self._neighbors]
        repr_tup = (title, neighbor_list)
        return str(repr_tup)

    def __len__(self):
        """
        :return: Integer size of neighbors dict.
        """
        return len(self._neighbors)

    def __contains__(self, item):
        """
        :return: True if article is in neighbors dict. (by object)
        """
        return item in self._neighbors.values()
