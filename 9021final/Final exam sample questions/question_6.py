# Will be tested with letters a string of DISTINCT UPPERCASE letters only.


def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution.
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # INSERT YOUR CODE HERE
    # 文件内容存储到集合中
    word_list = []
    with open(dictionary) as file:
        for line in file:
            line = line.strip()
            # 去掉有重复字母的单词
            word_dict = {}
            for char in line:
                if char not in word_dict:
                    word_dict[char] = 1
                else:
                    word_dict[char] = word_dict[char] + 1
            can_add = True
            for value in word_dict.values():
                if value != 1:
                    can_add = False
                    break
            if can_add:
                word_list.append(line)
    # 处理单词
    for i in range(len(word_list)):
        # 判断第一个单词是否在letters中
        word1_in_letters = True
        for char in word_list[i]:
            if char not in letters:
                word1_in_letters = False
        # 第一个单词在letters中
        if word1_in_letters:
            # letters去除第一个单词
            new_letters = ''
            for char in letters:
                if char not in word_list[i]:
                    new_letters += char
            # 看第二个单词是否在余下的字典中
            for j in range(i + 1, len(word_list)):
                if len(word_list[j]) == len(new_letters):
                    word2_in_letters = True
                    for char in word_list[j]:
                        if char not in new_letters:
                            word2_in_letters = False
                    if word2_in_letters:
                        solutions.append((word_list[i], word_list[j]))

    solutions = sorted(solutions)

    if not solutions:
        print('There is no solution.')
    else:
        print(f'The pairs of words using all (distinct) letters '
              f'in "{letters}" are:'
              )
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
