def get_word_count(file):
    with open(file) as f:
        word_list = f.read().split()
        return len(word_list)

def get_char_count(file):
    char_dict = dict()
    with open(file) as f:
       text = f.read()
       for c in text.lower():
          if c not in char_dict:
             char_dict[c] = text.lower().count(c)

    return char_dict

def sort_on(items):
    return items["num"]

def sorted_char_list(file):
    dict = get_char_count(file)
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "num": value})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
