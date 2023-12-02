# You can assume that the function is called with a strictly positive
# integer as first argument and either True or False as second argument,
# if any.


def rhombus(size, shift_right=False):
    '''
    >>> rhombus(1)
    A
    >>> rhombus(1, True)
    A
    >>> rhombus(2)
     BA
    CD
    >>> rhombus(2, True)
    AB
     DC
    >>> rhombus(3)
      CBA
     DEF
    IHG
    >>> rhombus(3, True)
    ABC
     FED
      GHI
    >>> rhombus(4)
       DCBA
      EFGH
     LKJI
    MNOP
    >>> rhombus(4, True)
    ABCD
     HGFE
      IJKL
       PONM
    >>> rhombus(7)
          GFEDCBA
         HIJKLMN
        UTSRQPO
       VWXYZAB
      IHGFEDC
     JKLMNOP
    WVUTSRQ
    >>> rhombus(7, True)
    ABCDEFG
     NMLKJIH
      OPQRSTU
       BAZYXWV
        CDEFGHI
         PONMLKJ
          QRSTUVW
    '''

    if shift_right == False:
        index = 65
        for i in range(size):
            word_str = ' ' * (size - 1 - i)
            # 偶数行颠倒输出
            if i % 2 == 0:
                new_str = ''
                for j in range(size):
                    new_str += chr(index)
                    index += 1
                    if index > 90:
                        index = 65
                # 颠倒
                for k in range(len(new_str) - 1, -1, -1):
                    word_str += new_str[k]
                print(word_str)
            else:
                for j in range(size):
                    word_str += chr(index)
                    index += 1
                    if index > 90:
                        index = 65
                print(word_str)

    else:
        index = 65
        for i in range(size):
            word_str = ' ' * i
            # 奇数行颠倒输出
            if i % 2 == 0:
                for j in range(size):
                    word_str += chr(index)
                    index += 1
                    if index > 90:
                        index = 65
                print(word_str)
            else:
                new_str = ''
                for j in range(size):
                    new_str += chr(index)
                    index += 1
                    if index > 90:
                        index = 65
                # 颠倒
                for k in range(len(new_str) - 1, -1, -1):
                    word_str += new_str[k]
                print(word_str)
    # chr() 获取字符
    # ord() 获取编号
    # 使用 reversed() 函数得到反转的迭代器。
    # 使用 join() 方法将迭代器中的元素组合成一个字符串。
    # REPLACE PASS ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
