from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6]]
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0]]
    >>> f(0, 4, 10)
    Here is L: [6, 6, 0, 4]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4]]
    >>> f(0, 5, 10)
    Here is L: [6, 6, 0, 4, 8]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8]]
    >>> f(0, 6, 10)
    Here is L: [6, 6, 0, 4, 8, 7]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8], [7]]
    >>> f(0, 7, 10)
    Here is L: [6, 6, 0, 4, 8, 7, 6]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[6], [0, 4, 8], [7], [6]]
    >>> f(3, 10, 6)
    Here is L: [1, 4, 4, 1, 2, 4, 3, 5, 4, 0]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[1, 4], [1, 2, 4], [3, 5], [4], [0]]
    >>> f(3, 15, 8)
    Here is L: [3, 8, 2, 5, 7, 1, 0, 7, 4, 8, 3, 3, 7, 8, 8]
    The decomposition of L into increasing sequences,
        with consecutive duplicates removed, is:
        [[3, 8], [2, 5, 7], [1], [0, 7], [4, 8], [3, 7, 8]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    # INSERT YOUR CODE HERE
    if nb_of_elements == 0:
        R = []
    elif nb_of_elements == 1:
        R = [L]
    else:
        remove_duplicates = [L[0]]
        for i in range(1, len(L)):
            if L[i] != L[i - 1]:
                remove_duplicates.append(L[i])
        # print(remove_duplicates)
        temp = []
        for i in range(len(remove_duplicates)):
            if i != len(remove_duplicates) - 1:
                if remove_duplicates[i] < remove_duplicates[i + 1]:
                    temp.append(remove_duplicates[i])
                else:
                    temp.append(remove_duplicates[i])
                    R.append(temp)
                    temp = []
            else:
                if temp is None:
                    temp = [remove_duplicates[-1]]
                    R.append(temp)
                else:
                    temp.append(remove_duplicates[-1])
                    R.append(temp)

    """
    if nb_of_elements == 0:
        R = []
    elif nb_of_elements == 1:
        R = [L]
    else:
        remove_duplicates = [L[0]]
        for i in range(1,len(L)):
            if L[i] != L[i-1]:
                remove_duplicates.append(L[i])
        
        temp = [remove_duplicates[0]]
        for i in range(1,len(remove_duplicates)):
            if remove_duplicates[i] > remove_duplicates[i-1]:
                temp.append(remove_duplicates[i])
            else:
                R.append(temp)
                temp = [remove_duplicates[i]]
        
        if temp:
            R.append(temp)
    
    """

    print('The decomposition of L into increasing sequences,')
    print('    with consecutive duplicates removed, is:\n   ', R)


# f(3,10,6)
# f(3,15,8)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
