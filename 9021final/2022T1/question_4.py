from itertools import zip_longest


# The carry over of the sum of all units is discarded.
# The carry over of the sum of all multiples of 10 is discarded.
# The carry over of the sum of all multiples of 100 is discarded.
# ...
# Will be tested with at least one argument,
# all arguments being positive integers (possibly equal to 0).

def sum_discarding_carry_overs(*numbers):
    '''
    >>> sum_discarding_carry_overs(0)
    0
    >>> sum_discarding_carry_overs(3, 4)
    7
    >>> sum_discarding_carry_overs(4, 6)
    0
    >>> sum_discarding_carry_overs(7, 5)
    2
    >>> sum_discarding_carry_overs(0, 1, 2, 3)
    6
    >>> sum_discarding_carry_overs(0, 1, 2, 3, 4)
    0
    >>> sum_discarding_carry_overs(0, 1, 2, 3, 4, 5)
    5
    >>> sum_discarding_carry_overs(91, 19)
    0
    >>> sum_discarding_carry_overs(38, 49)
    77
    >>> sum_discarding_carry_overs(58, 59)
    7
    >>> sum_discarding_carry_overs(2314, 5968)
    7272
    >>> sum_discarding_carry_overs(3452, 2324, 36372, 75401)
    6449
    >>> sum_discarding_carry_overs(9054, 3, 3577, 78, 452563)
    454055
    '''
    num_list = []
    length = 0
    for num in numbers:
        num = str(num)
        if len(num) > length:
            length = len(num)
        num_list.append(num)

    for i in range(len(num_list)):
        num_length = len(num_list[i])
        if num_length != length:
            zeroes = (length - num_length) * '0'
            num_list[i] = zeroes + num_list[i]

    final_str = ''

    for i in range(length):
        part_sum = 0
        for j in range(len(num_list)):
            part_sum += int(num_list[j][i])
        part_sum = str(part_sum)[-1]
        final_str += part_sum

    return int(final_str)

    # return -1
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
