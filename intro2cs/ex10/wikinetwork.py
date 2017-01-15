"""########################################################################
# FILE : wikinetwork.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION: ----
########################################################################"""
# ========== IMPORTS ======================================================
import article
import copy

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
        for line in f:
            line = line.strip('\n')
            pair = line.split('\t')
            pair_tup = tuple(pair)
            pairs.append(pair_tup)
    return pairs

# ========== CLASS WIKI NETWORK ===========================================


class WikiNetwork:
    """
    A graph-like data structure,
    representing the connectivity of a wikipedia-like
    collection of articles.
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

        :param title:
        :return:
        """
        if title in self._articles:
            return self._articles[title]
        else:
            raise KeyError(title)

    def page_rank(self, iters, d=0.9):
        """
        Ranks all pages using the Page Rank algorithm.
        :param iters: number of desired iterations.
        :param d: Amount of equally divided (communist) money
        :return: sorted list of titles, by page rank
        """
        rank_dict = {x: 1 for x in self.get_titles()}
        adder_dict = {x: 0 for x in self.get_titles()}
        for x in range(iters):
            for title in rank_dict:
                neighbor_num = len(self._articles[title])
                give_amount = 0
                if neighbor_num != 0:
                    give_amount = d * (rank_dict[title] / neighbor_num)
                rank_dict[title] = 0
                neighbor_titles = [x.get_title() for x in
                                   self._articles[title].get_neighbors()]
                for y in neighbor_titles:
                    adder_dict[y] += give_amount
            for title in adder_dict:
                rank_dict[title] = adder_dict[title] + (1-d)
        # Sorting: -x[0] to sort by rank - descending,
        # and then by abc, ascending,
        ranking = sorted(rank_dict.items(), key=lambda x: (-x[1], x[0]),)
        ranked_list = [x[0] for x in ranking]
        return ranked_list

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
            neighbor_titles = [x.get_title() for x in
                               self._articles[title].get_neighbors()]
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
        # Sorting: -x[0] to sort by rank - descending,
        # and then by abc, ascending,
        ranking = sorted(rank_dict.items(), key=lambda x: (-x[1], x[0]),)
        ranked_list = [x[0] for x in ranking]
        return ranked_list

    def _update_entry_index(self):
        """

        :return:
        """
        entry_dict = {x: 0 for x in self.get_titles()}
        for page in self._articles:
            for neighbor in self._articles[page].get_neighbors():
                entry_dict[neighbor.get_title()] += 1
        self._entry_index = entry_dict

    def travel_path_iterator(self, article_title):
        """

        :param article_title:
        :return:
        """
        if article_title not in self:
            return None
        yield article_title
        self._update_entry_index()
        entry_dict = copy.copy(self._entry_index)
        curr_art = self._articles[article_title]
        neighbor_list = [x.get_title() for x in curr_art.get_neighbors()]
        while neighbor_list:
            entry_dict = copy.copy(self._entry_index)
            filtered = {k: v for k, v in entry_dict.items()
                        if k in neighbor_list}
            ranked = sorted(filtered.items(),
                            key=lambda x: (-x[1], x[0]), )
            ranked_list = [x[0] for x in ranked]
            max_title = ranked_list[0]
            yield max_title
            curr_art = self._articles[max_title]
            neighbor_list = [x.get_title() for x in curr_art.get_neighbors()]
