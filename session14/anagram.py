

def file_to_list(filename):
    
    with open(filename) as f:
        l = f.read().splitlines() 
    return l

def sort_word(word_list):
    for t in word_list:
        t = list(word_list)
        t.sort()
        t = ''.join(t)
    return t

def list_to_dict(wordlist):
    pass

def main():
    word_list = file_to_list('data/words')
    sorted_list = sort_word(word_list)
    print(sorted_list)

if __name__ == "__main__":
    main()