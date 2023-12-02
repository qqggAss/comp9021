# Will be tested with height a strictly positive integer.


def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''
    # INSERT YOUR CODE HERE
    modify_height = height - 1
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    index = 0
    for i in range(height):
        front_blank = ' ' * (modify_height - i)
        # back_blank = ' '*(modify_height-i)
        num_str = ''
        for j in range(2 * i + 1):
            num_str += num_list[index]
            index += 1
            if index > 9:
                index = 0
        # print(front_blank + num_str + back_blank)
        print(front_blank + num_str)
        '''
        不需要后面的空格

        '''


if __name__ == '__main__':
    import doctest

    doctest.testmod()
