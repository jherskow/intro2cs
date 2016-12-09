##########################################################################
# FILE : ex5.py
# WRITER : Avraham Sagal, avisa, 302931613
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex5 2016-2017
# DESCRIPTION:
##########################################################################
import xml.etree.ElementTree as Et

EMPTY_STRING = ""
# We did NOT use a constant for empty dictionary because doing so
# interacted unexpectedly with the xml library. Sorry.


def get_attribute(store_db, ItemCode, tag):
    """
    Returns the attribute (tag) 
    of an Item with code: Itemcode in the given store
    """
    tag_value = store_db[ItemCode][tag]
    return tag_value


def string_item(item):
    """
    Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'
    """
    item_code = item["ItemCode"]
    item_name = item["ItemName"]
    return "[" + item_code + "]\t{" + item_name + "}"
  

def string_store_items(store_db):
    """
    Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    """
    inventory = EMPTY_STRING
    for item in store_db:
        # since item is only the key in store_db, de need to specify
        # in order to pass the entire dictionary of the item
        inventory += string_item(store_db[item]) + "\n"
    return inventory


def read_prices_file(filename):
    """
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad haclcala".
    Returns a tuple: store_id and a store_db,
    where the first variable is the store name
    and the second is a dictionary describing the store.
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    """
    tree = Et.parse(filename)
    root = tree.getroot()
    store_name = EMPTY_STRING
    store_db = {}
    for child in root:
        if child.tag == 'StoreId':
            store_name = child.text
    for item in root.find('Items').findall('Item'):
        item_code = item.find('ItemCode').text
        item_dic = {}
        for child in item:
            property_tag = child.tag
            property_value = child.text
            item_dic[property_tag] = property_value
        store_db[item_code] = item_dic
    return store_name, store_db


def filter_store(store_db, filter_txt):  
    """
    Create a new dictionary that includes only the items 
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName. 
    Args:
    store_db: a dictionary of dictionaries as created in read_prices_file.
    filter_txt: the filter text as given by the user.
    """
    filtered_store = {}
    for item_code in store_db:
        if filter_txt in store_db[item_code]['ItemName']:
            filtered_store[item_code] = store_db[item_code]
    return filtered_store


def create_basket_from_txt(basket_txt):
    """
    Receives text representation of few items (and maybe some garbage
      at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt
    """
    between_delimiters = False
    basket = []
    word = EMPTY_STRING
    for letter in basket_txt:
        if letter == "[":
            between_delimiters = True
        elif letter == "]":
            if between_delimiters:
                basket.append(word)
                between_delimiters = False
                word = EMPTY_STRING
        elif between_delimiters:
            word += letter
    return basket


def get_basket_prices(store_db, basket):  # todo WTF
    """
    Arguments: a store - dictionary of dictionaries and a basket - 
       a list of ItemCodes
    Go over all the items in the basket and create a new list 
      that describes the prices of store items
    In case one of the items is not part of the store, 
      its price will be None.
    """
    price_list = []
    for i, item_code in enumerate(basket):
        price = store_db[item_code]['ItemPrice']
        price = float(price)
        price_list.append(price)
    return price_list


def sum_basket(price_list):
    """
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones) 
      and the number of missing items (Number of Nones)

    """
    pass 

 
def basket_item_name(stores_db_list, ItemCode):
    """ 
    stores_db_list is a list of stores (list of dictionaries of 
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not avaiable in any of the stores return only [ItemCode]
    """
    pass


def save_basket(basket, filename):
    """ 
    Save the basket into a file
    The basket representation in the file will be in the following format:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    """
    pass


def load_basket(filename):
    """ 
    Create basket (list of ItemCodes) from the given file.
    The file is assumed to be in the format of:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    """
    pass
 

def best_basket(list_of_price_list):
    """
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a 
    missing item has a price of its maximal price in the other stores *1.25

    """ 
    pass

''' ========================DAAANGEEERRRR ZOOOONE++++++++++++++++++++++++++
x = read_prices_file('/cs/usr/jherskow/safe/intro2cs/ex5/Store_1.xml')
print(string_store_items(x[1]))
create_basket_from_txt(basket_txt):

basket_txt = "[66196] {לירג ילסיב} [30794] {היוס הקשמ} [556"
x= create_basket_from_txt(basket_txt)
print(x)



b = '907]	{תיתחפשמ הציפ}[66196]	{לירג ילסיב}[84316]	'
c = '96]	{לירג ילסיב}[84316]	{רטיל 5.1 קובקב הלוק הקוק}[59907]	{תיתחפשמ הציפ}[13520]	{סקלפנרוק קילק}'

print(create_basket_from_txt(b))
print(create_basket_from_txt(c))


'''