""" test for ex10 """
import article
import wikinetwork

file = '/cs/usr/jherskow/safe/intro2cs/ex10/links.txt'
link_list = wikinetwork.read_article_links(file)
new_net = wikinetwork.WikiNetwork(link_list)
print(new_net)