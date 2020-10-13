def make_dict_key(dic):
    word_list = []
    
    for key in open(dic):
        
        if len(key) > 1:
            word = key.strip()
            word_list.append((len(key), word))

    word_list.sort()
    
    return word_list

print(make_dict_key('data/words.txt'))

def has_duplicates(s):
    d = {}
    for i in s:
        if i in d:
            return True
        d[i] = True
    return False

print(has_duplicates(open('data/words.txt')))