def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    s = 0
    for i in t:
        if isinstance(i, list):
            s += nested_sum(i)
        else:
            s += i 
    return s


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    s = 0
    cum = []
    length = len(t)
    for i in range(length):
        s += t[i]
        cum.append(s)
    return cum


def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return t[1:-1]


def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t.remove(t[0])
    t.pop()
    return t


def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    s = t[:]
    s.sort()
    if s == t:
        return True
    else:
        return False
    


def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    length_w1 = len(word1)
    length_w2 = len(word2)

    if length_w1 != length_w2:
        return False
    
    for i in range(length_w1):
        if sorted(word1) == sorted(word2):
            return True
        else:   
            return False


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool

    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    for i in s:
        if s.count(i) > 1:
            return True
    return False


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.

    s: string or list

    returns: bool

    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    length = len(s)

    for i in range(length - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

    print(has_adjacent_duplicates('cba'))
    print(has_adjacent_duplicates('abca'))
    print(has_adjacent_duplicates('abbc'))


if __name__ == "__main__":
    main()
