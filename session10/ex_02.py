#exercise 2
def count(word,letter):
    """
    Count selected letter in a given word. 
    """
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)




def main(): 
    count('Facebook','')

if __name__ == "__main__":
    main()