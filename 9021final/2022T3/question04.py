# Final Exam Question 4

'''
No point to hard code for small values of n, will be tested
only for large enough values...
'''


def pascal_triangle_line(n):
    '''
    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''

    list_result = []
    m = 0
    while m != n:
        num = C_m_n(n - 1, m)
        list_result.append(num)
        m += 1
    return list_result
    # REPLACE return WITH YOUR CODE


def factor(n):
    if n == 1:
        return 1
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def C_m_n(n, m):
    return int(factor(n) / (factor(n - m) * factor(m)))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
