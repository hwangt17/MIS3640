def rotate_word(word,num):
    """
    this is a function that takes a string and an integer as parameters, and returns a new string that contains the letters from the original string rotated by the given amount.
    """
    index = ''

    for i in range(len(word)):
        char = word[i]
        if char.isupper():
            index = index + chr((ord(char) + num - 65) % 26 + 65) #rotate CAP numbers
        else:
            index = index + chr((ord(char) + num - 97) % 26 + 97) #rotate noCAP number
    return index


def main(): 
    print(rotate_word('dhvpx', 13))

if __name__ == "__main__":
    main()