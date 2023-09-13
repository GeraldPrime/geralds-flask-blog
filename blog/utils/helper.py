def find_item_in_list(list, cb):
    for index, item in enumerate(list):
        if cb(item, index, list): 
            return item
