# The words in the file are supposed to consist of nothing but letters
# (no apostrophes, no hyphens...), possibly immediately followed by
# a single full stop, exclamation mark, question mark,
# comma, colon or semicolon.
#
# There can be any amount of space anywhere between words, before the
# first word, and after the last word.
#
# We do not distinguish between words that only differ in cases.
# For instance, millionaires, Millionaires, MILLIONAIRES are
# 3 variants of the same word.
#
# You can assume that filename is the name of a file that exists
# in the working directory. Do NOT use an absolute path.
#
# The words of length greater than 2 are checked against the contents
# of dictionary.txt, also assumed to be stored in the working directory.
# Here too, do NOT use an absolute path.
#
# Unknown words (that is, words of length greater than 2 that are
# not found in dictionary.txt) are output only once, in capitalised form,
# in lexicographic order for each group, a group consisting of words
# all of the same length.
# Groups for shorter words are output before groups for longer words.

# Note that no tab is output anywhere, just single spaces.


from collections import defaultdict


def unknown_words(filename):
    '''
    >>> unknown_words('edgar_poe_1.txt')
    There are no unknown words of length greater than 2.
    >>> unknown_words('edgar_poe_2.txt')
    There are unknown words of length greater than 2.
      - Of length 8:
          Practise
      - Of length 9:
          Fortunato
          Imposture
          Redresser
      - Of length 10:
          Immolation
      - Of length 11:
          Unredressed
      - Of length 12:
          Definitively
      - Of length 14:
          Definitiveness
      - Of length 15:
          Connoisseurship
    >>> unknown_words('oscar_wild_1.txt')
    There are no unknown words of length greater than 2.
    >>> unknown_words('oscar_wild_2.txt')
    There are unknown words of length greater than 2.
      - Of length 5:
          Renan
      - Of length 7:
          Realise
      - Of length 8:
          Flaubert
      - Of length 10:
          Neighbours
      - Of length 11:
          Misdirected
    '''
    # 添加到字典中
    dic_file = 'dictionary.txt'
    dictionary = set()
    with open(dic_file) as file:
        for line in file:
            line = line.strip()
            dictionary.add(line)

    text_list = []

    # 读文件
    with open(filename) as file:
        for line in file:
            if not line.isspace():
                line = line.split()
                text_list.extend(line)

    for i in range(len(text_list)):
        if text_list[i][-1] == ',' or text_list[i][-1] == '.' or text_list[i][-1] == '!' \
                or text_list[i][-1] == ';' or text_list[i][-1] == '?' or text_list[i][-1] == ':':
            text_list[i] = text_list[i][:-1]
        text_list[i] = text_list[i].upper()

    # print(text_list)

    unknown = set()
    length_set = set()

    for char in text_list:
        if char not in dictionary:
            if len(char) > 2:
                upper_part = char[0].upper()
                lower_part = char[1:len(char)].lower()
                word = upper_part + lower_part
                unknown.add(word)
                length_set.add(len(word))

    # print(unknown)
    # print(length_set)

    if len(unknown) == 0:
        print('There are no unknown words of length greater than 2.')
    else:
        print('There are unknown words of length greater than 2.')
        length_list = sorted(list(length_set))
        for i in range(len(length_list)):
            print(' ' * 2 + f'- Of length {length_list[i]}:')
            word_list = []
            for item in unknown:
                if len(item) == length_list[i]:
                    word_list.append(item)
            word_list = sorted(word_list)
            for j in range(len(word_list)):
                print(' ' * 6 + f'{word_list[j]}')

    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
