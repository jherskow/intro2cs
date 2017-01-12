""" test for ex10 """
import article
import wikinetwork

file = 'ex10/links.txt'
link_list = wikinetwork.read_article_links(file)
new_net = wikinetwork.WikiNetwork()
print(new_net)