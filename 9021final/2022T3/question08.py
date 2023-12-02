# COMP9021 2022T3 - Rachid Hamadi
# Final Exam Question 8

def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.

    Conjunctions of inputs will be tested, so hard coding will not help.

    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    result_set = set()
    num_of_result = len(square) * 2 + 2
    # 计算 行
    for i in range(len(square)):
        row_sum = 0
        for j in range(len(square)):
            row_sum += square[i][j]
        result_set.add(row_sum)
    # 计算 列
    for i in range(len(square)):
        column_sum = 0
        for j in range(len(square)):
            column_sum += square[j][i]
        result_set.add(column_sum)
    # 计算 对角
    xiebian_sum1 = 0
    for i in range(len(square)):
        xiebian_sum1 += square[i][i]
    result_set.add(xiebian_sum1)

    xiebian_sum2 = 0
    row = 0
    for i in range(len(square) - 1, -1, -1):
        xiebian_sum2 += square[row][i]
        row += 1
    result_set.add(xiebian_sum2)

    if len(result_set) == num_of_result:
        return True
    else:
        return False

    # REPLACE return WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest

    doctest.testmod()
