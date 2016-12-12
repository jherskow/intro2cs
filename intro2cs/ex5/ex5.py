##########################################################################
# FILE : ex5.py
# WRITER : Avraham Sagal, avisa, 302931613
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex5 2016-2017
# DESCRIPTION:
##########################################################################
import xml.etree.ElementTree as Et

EMPTY_STRING = ""
EMPTY_LIST = []
EMPTY_DICT = {}
PENALTY_MODIFIER = 1.25


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
    if store_db == EMPTY_DICT:
        return EMPTY_STRING
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
    store_db = dict()
    for child in root:
        if child.tag == 'StoreId':
            store_name = child.text
    for item in root.find('Items').findall('Item'):
        item_code = item.find('ItemCode').text
        item_dic = dict()
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
    filtered_store = dict()
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
    basket = EMPTY_LIST
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


def get_basket_prices(store_db, basket):
    """
    Arguments: a store - dictionary of dictionaries and a basket -
       a list of ItemCodes
    Go over all the items in the basket and create a new list
      that describes the prices of store items
    In case one of the items is not part of the store,
      its price will be None.
    """
    price_list = EMPTY_LIST
    for i, item_code in enumerate(basket):
        if item_code in store_db:
            price = store_db[item_code]['ItemPrice']
            price = float(price)
            price_list.append(price)
        else:
            price_list.append(None)
    return price_list


def sum_basket(price_list):
    """
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones)
      and the number of missing items (Number of Nones)

    """
    nun_counter = 0
    sum = 0
    for price in price_list:
        if price is None:
            nun_counter += 1  # add one to the nunnery
        else:
            sum += price
    return sum, nun_counter


def basket_item_name(stores_db_list, ItemCode):
    """
    stores_db_list is a list of stores (list of dictionaries of
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not avaiable in any of the stores return only [ItemCode]
    """
    for i, store in enumerate(stores_db_list):
        if ItemCode in stores_db_list[i]:
            return string_item(stores_db_list[i][ItemCode])
    return '[' + ItemCode + ']'


def save_basket(basket, filename):
    """
    Save the basket into a file
    The basket representation in the file will be in the following format:
    [ItemCode1]
    [ItemCode2]
    ...
    [ItemCodeN]
    """
    with open(filename, 'w') as file:
        for item_code in basket:
            file.write('[' + item_code + ']\n')
    file.close
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
    with open(filename, 'r') as file:
        file_string = file.read()
        basket = create_basket_from_txt(file_string)
    return basket


def best_basket(list_of_price_list):
    """
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a
    missing item has a price of its maximal price in the other stores *1.25
    """
    item_prices = EMPTY_LIST
    copy_lopl = list_of_price_list[:]
    copy_lopl = none_to_zero(copy_lopl)
    item_prices = price_array(copy_lopl, item_prices)
    copy_lopl = penalize(copy_lopl, item_prices)
    all_stores_sum = stores_sum(copy_lopl)
    # this part of the function finds the cheapest store
    best_store = min(all_stores_sum)
    for i, store in enumerate(all_stores_sum):
        if all_stores_sum[i] == best_store:
            return i


# ================= BEST BASKET HELPER FUNCTIONS ==========================


def none_to_zero(list_of_price_list):
    """
    This function swaps all "None" in a list with "0"
    and returns the modified list.
    """
    new_list_of_price_list = EMPTY_LIST
    for i, store in enumerate(list_of_price_list):
        new_store = EMPTY_LIST
        for j, num in enumerate(store):
            if num is None:
                new_store.append(0)
            else:
                new_store.append(num)
        new_list_of_price_list.append(new_store)
    return new_list_of_price_list


def price_array(copy_lopl, item_prices):
    """
    Returns a list of lists, where each sub-list is a list of the
    i-th items prices in all stores, so that the max() method
    can then be used
    """
    new_list = EMPTY_LIST
    for i in range(len(copy_lopl[0])):
        for j, num in enumerate(copy_lopl):
            new_list.append(copy_lopl[j][i])
        item_prices.append(new_list)
        new_list = EMPTY_LIST
    return item_prices


def penalize(copy_lopl, item_prices):
    """
    This function replaces all 0 prices with the penalized price.
    """
    for i, store in enumerate(copy_lopl):
        for j, price in enumerate(store):
            if price is 0:
                store[j] = (max(item_prices[j])) * PENALTY_MODIFIER
    return copy_lopl


def stores_sum(copy_lopl):
    all_stores_sum = EMPTY_LIST
    for i, store in enumerate(copy_lopl):
        sum_store = sum(store)
        all_stores_sum.append(sum_store)
    return all_stores_sum


# ============= END BEST BASKET HELPER FUNCTIONS ==========================
