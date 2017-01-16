""" test for ex10 """
import article
import wikinetwork

file = 'links.txt'
link_list = wikinetwork.read_article_links(file)
new_net = wikinetwork.WikiNetwork(link_list)
length = len(new_net)
x = len(new_net.friends_by_depth('United_States', 1))
y = len(new_net.friends_by_depth('United_States_dollar', 2))
z = len(new_net.friends_by_depth('Microsoft', 3))
print(str(x) + ' / ' + str(length) + ' = ' + str(x/length) + ' = ' + str((x/length)*100) + '%')
print(str(y) + ' / ' + str(length) + ' = ' + str(y/length) + ' = ' + str((y/length)*100) + '%')
print(str(z) + ' / ' + str(length) + ' = ' + str(z/length) + ' = ' + str((z/length)*100) + '%')
