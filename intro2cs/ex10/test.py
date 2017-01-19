""" test for ex10 """
import article
import wikinetwork

file = 'links.txt'
link_list = wikinetwork.read_article_links(file)
new_net = wikinetwork.WikiNetwork(link_list)
length = len(new_net)
for thing in new_net.travel_path_iterator('Fiji'):
    print(thing)
