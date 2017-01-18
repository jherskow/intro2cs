"""########################################################################
# FILE : wikinetwork.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION: Implements wikinetwork object and functionality.
########################################################################"""
# ========== IMPORTS ======================================================
import article
import copy

# ============================ CLASS WIKI NETWORK =========================


class WikiNetwork:
    """
    A graph-like data structure,
    representing the connectivity of a wikipedia-like
    collection of articles.
    """

    # ===== WikiNetwork - class constants =====
    PAIR_SEPARATOR = '\t'
    DEFAULT_ALTRUISM = 0.9

    # ===== WikiNetwork - class methods =======

    def __init__(self, link_list):
        """
        Initialize a new WikiNetwork.
        :param link_list: A text file in compatible format.
        """
        self._articles = dict()
        self.update_network(link_list)
        self._entry_index = dict()

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
            if self._articles[link[1]] not in self._articles[link[0]]:
                self._articles[link[0]].\
                        add_neighbor(self._articles[link[1]])

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

    def __contains__(self, title):
        """
        :param title: An Article title..
        :return: True if article in network. (by title)
        """
        return title in self._articles

    def __len__(self):
        """
        :return: Integer size of network.
        """
        return len(self._articles)

    def __repr__(self):
        """
        Returns a string of a dictionary.
        The keys are the articles.
        The values are the articles' string representation.
        :return: String of dictionary.
        """
        repr_dict = {x: self._articles[x] for x in self._articles}
        return str(repr_dict)

    def __getitem__(self, title):
        """
        Returns an article with a given title, if it exists.
        :param title: Article title.
        :return: Article object
        """
        if title in self._articles:
            return self._articles[title]
        else:
            raise KeyError(title)

    def page_rank(self, iters, d=DEFAULT_ALTRUISM):
        """
        Ranks all pages using the Page Rank algorithm.
        :param iters: number of desired iterations.
        :param d: Amount of equally divided (communist) money
        :return: sorted list of titles, by page rank
        """
        rank_dict = {x: 1 for x in self.get_titles()}
        adder_dict = {x: 0 for x in self.get_titles()}
        for i in range(iters):
            for title in rank_dict:
                neighbor_num = len(self._articles[title])
                give_amount = 0
                if neighbor_num != 0:
                    give_amount = d * (rank_dict[title] / neighbor_num)
                rank_dict[title] = 0
                neighbor_list = self._articles[title].get_neighbors()
                neighbor_titles = self.title_list(neighbor_list)
                for y in neighbor_titles:
                    adder_dict[y] += give_amount
            for title in adder_dict:
                rank_dict[title] = adder_dict[title] + (1-d)
        return self.sort_dict_by_rank(rank_dict, return_list=True)

    def jaccard_index(self, article_title):
        """
        Ranks all articles by jaccard index to a specific given article.
        :param article_title: title of an article in network
        :return: list of article titles, sorted by jaccard index,
                  in relation to the given article.
        """
        if article_title not in self:
            return None
        if len(self._articles[article_title].get_neighbors()) == 0:
            return None
        rank_dict = {x: 0 for x in self.get_titles()}
        set_dict = dict()
        # Create a dictionary of titles and sets.
        for title in rank_dict:
            neighbor_list = self._articles[title].get_neighbors()
            neighbor_titles = self.title_list(neighbor_list)
            set_dict[title] = set(neighbor_titles)
        compare_set = set_dict[article_title]
        # Calculate ranking values to each article, & save in rank_dict
        for art_set in set_dict:
            intersection = set_dict[art_set].intersection(compare_set)
            union = set_dict[art_set].union(compare_set)
            if len(union) != 0:
                rank_dict[art_set] = len(intersection) / len(union)
            else:
                rank_dict[art_set] = len(intersection)
        return self.sort_dict_by_rank(rank_dict, return_list=True)

    def _update_entry_index(self):
        """
        updates the entry index of all articles on the network.
        Stored as a title: entry_index dictionary.
        """
        entry_dict = {x: 0 for x in self.get_titles()}
        for page in self._articles:
            for neighbor in self._articles[page].get_neighbors():
                entry_dict[neighbor.get_title()] += 1
        self._entry_index = entry_dict

    def travel_path_iterator(self, article_title):
        """
        Generates the title of the neighboring article
        with the highest entry index.
        :param article_title: title of an article
        :return: title of article.
        """
        if article_title not in self:
            return None
        yield article_title
        self._update_entry_index()
        curr_art = self._articles[article_title]
        neighbor_lst = self.title_list(curr_art.get_neighbors())
        while neighbor_lst:
            entry_dict = copy.copy(self._entry_index)
            filtered = {k: v for k, v in entry_dict.items()
                        if k in neighbor_lst}
            max_title = self.sort_dict_by_rank(filtered, return_top=True)
            yield max_title
            curr_art = self._articles[max_title]
            neighbor_lst = self.title_list(curr_art.get_neighbors())

    def friends_by_depth(self, article_title, depth):
        """
        Returns a list of titles of all articles within x 'jumps'
        from a given article.
        :param article_title: An article's title.
        :param depth: integer of 'jumps'
        :return: list of article titles.
        """
        if article_title not in self:
            return None
        article_list = [self._articles[article_title]]
        friends = self._recursive_friends_set(article_list, depth)
        friends.add(self._articles[article_title])
        friend_titles = self.title_list(friends)
        return friend_titles

    def _recursive_friends_set(self, article_list, depth):
        """
        Returns all articles (except self) that are within a maximum depth.
        :param article_list: list of article objects.
        :param depth: desired depth
        :return: set of articles of depth <= depth
        """
        if depth == 0:
            return set()
        friends = set()
        for art in article_list:
            friends.update(art.get_neighbors())
        friends.update(self._recursive_friends_set(friends, depth - 1))
        return friends

    # ===== WikiNetwork - required functions ========

    def read_article_links(self, filename):
        """
        Converts text file of compatible format into
        a list of article-pair tuples.
        :param filename: text file of compatible format
        :return: list of (article,pair) tuples
        """
        pairs = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                pair = line.split(self.PAIR_SEPARATOR)
                pair_tup = tuple(pair)
                pairs.append(pair_tup)
        return pairs

    # ===== WikiNetwork - helper functions ================
    @staticmethod
    def sort_dict_by_rank(dictionary, return_top=False, return_list=False):
        """
        Sorts a dictionary by rank, descending
        and then by abc, ascending.
        :param dictionary: a title: rank dictionary.
        :param return_top: bool
        :param return_list: bool
        :return: first value, or list, depending on user's choice of param.
        """
        ranked = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
        ranked_list = [x[0] for x in ranked]
        if return_top:
            return ranked_list[0]
        if return_list:
            return ranked_list

    @staticmethod
    def title_list(article_list):
        """
        Returns a list of titles from a list of articles.
        :param: article list:  list of article objects.
        :return: list of titles of articles in list.
        """
        return [x.get_title() for x in article_list]
