def get_num_words(text_string):
    return (len(text_string.split()))

def count_symbols(text_string):
    text_string = text_string.lower()
    all_symbols = {}
    for s in text_string:
        if s not in all_symbols:
            all_symbols[s] = 0
        all_symbols[s] += 1
    
    return all_symbols




def sort_on(items):
    return items["num"]

def sort_dictionary(letters_dict):

    letters_dict_list = []
    for entry in letters_dict:
        letters_dict_list.append({"letter": entry, "num": letters_dict[entry]})

    letters_dict_list.sort(reverse=True, key=sort_on)
    return letters_dict_list