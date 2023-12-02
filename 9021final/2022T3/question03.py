# COMP9021 2022T3 - Rachid Hamadi
# Final Exam Question 3

'''
You might find the ord() function useful.
'''


def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''
    if word == '':
        return ''
    else:
        sequence = []
        pre_index = ord(word[0])
        temp = [word[0]]
        for i in range(1, len(word)):
            now_index = ord(word[i])
            if now_index == pre_index + 1:
                temp.append(word[i])
            else:
                sequence.append(temp)
                temp = [word[i]]
            pre_index = ord(word[i])
        if temp:
            sequence.append(temp)
        length = []
        for i in range(len(sequence)):
            length.append(len(sequence[i]))
        max_length = max(length)
        longest_str = ''
        for i in range(len(sequence)):
            if len(sequence[i]) == max_length:
                for j in range(len(sequence[i])):
                    longest_str += sequence[i][j]
                break

        return longest_str


# REPLACE return WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
