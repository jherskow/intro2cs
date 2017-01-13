""" test for ex10 """
import article
import wikinetwork

file = 'links.txt'
link_list = wikinetwork.read_article_links(file)
new_net = wikinetwork.WikiNetwork(link_list)
ls = (new_net.get_articles())
#for x in ls:
#    print(x)
lista = new_net.page_rank(10)
for i, title in enumerate(lista):
    print(str(i) + title)
print(str(len(new_net)))