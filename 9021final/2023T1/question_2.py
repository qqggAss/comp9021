# Given a dictionary D and a key x, there is a (unique) loop
# containing x if there are keys x_1, ..., x_k such that:
# D maps x to x_1
# D maps x_1 to x_2
# ...
# D maps x_{k-1} to x_k
# x_1, ..., x_{k-1} are all different to x and x_k is x
# (in the particular case where k = 1, D maps x to x).
#
# When the loop does not exist, the function prints out nothing.
# When the loop exists, the function prints out the loop,
# STARTING AND ENDING with the SMALLEST element in the loop.
#
# You can assume that the function is called with as first argument,
# a dictionary having nothing but integers as keys and values,
# and with as second argument, an integer.


def loop(D, x):
    '''
    >>> loop({1: 1}, 0)
    >>> loop({1: 2, 2: 2}, 1)
    >>> loop({1: 2, 2: 3}, 1)
    >>> loop({1: 2, 2: 3, 3: 2}, 1)
    >>> loop({1: 1}, 1)    
    1--1
    >>> loop({1: 2, 2: 1}, 2)
    1--2--1
    >>> loop({12: 14, 13: 14, 14: 7, 7: 12, 6: 8, 8: 6, 5: 11}, 14)
    7--12--14--7
    >>> loop({0: 4, 1: 0, 2: 1, 3: 2, 4: 7, 5: 6, 6: 4, 7: 0, 8: 8, 9: 4}, 4)
    0--4--7--0
    >>> loop({0: 7, 1: 7, 2: 3, 3: 8, 4: 6, 5: 8, 6: 6, 7: 4, 8: 9, 9: 2}, 8)
    2--3--8--9--2
    '''
    result = None
    if x in D:
        loop_list = [x]
        while loop_list[-1] in D:
            value = D[loop_list[-1]]
            if value == loop_list[0]:
                loop_list.append(value)
                result = loop_list
                break
            elif value in loop_list:
                break
            else:
                loop_list.append(value)

    if result:
        final_list = []
        loop_list = sorted(loop_list)
        for i in range(len(loop_list)):
            if i == 0:
                final_list.append(str(loop_list[i]))
            else:
                if loop_list[i] != loop_list[i - 1]:
                    final_list.append(str(loop_list[i]))
        final_list.append(str(loop_list[0]))

        final_str = '--'.join(final_list)

        print(final_str)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
