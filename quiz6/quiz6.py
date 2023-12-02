# Written by *** for COMP9021
#
# Identifies in a grid the rhombuses (of any size)
# that are not included in any other rhombus.
#
# This is a rhombus of size 1:
#        *
#      *   *
#        *
#
# This is a rhombus of size 2:
#        *
#      *   *
#    *       *
#      *   *
#        *


from collections import defaultdict
from random import seed, randrange
import sys


def display_grid():
    print('  ', '-' * (2 * dim + 3))
    for row in grid:
        print('   |', *row, '|')
    print('  ', '-' * (2 * dim + 3))


try:
    for_seed, density, dim = (int(x)
                              for x in input('Enter three integers, '
                                             'the second and third ones '
                                             'being strictly positive: '
                                             ).split()
                              )
    if density <= 0 or dim <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [['*' if randrange(density) != 0 else ' ' for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
display_grid()

results = defaultdict(list)


# INSERT YOUR CODE HERE
# top_vertex = []
# for i in range(dim):
#     for j in range(dim):
#         # 左下方和右下方都有*
#         if grid[i][j] == '*':
#             # size = 1
#             # if (i < dim - 1 and j > 0 and grid[i + 1][j - 1] == '*') and \
#             #         (i < dim - 1 and j < dim - 1 and grid[i + 1][j + 1] == '*'):
#             #     if i + 2 <= dim - 1 and grid[i + 2][j] == '*':
#             #         top_vertex.append((i, j))
#             if (i < dim - 1 and j > 0 and grid[i + 1][j - 1] == '*'):
#                 pass
#             else:
#                 continue
#             if (i < dim - 1 and j < dim - 1 and grid[i + 1][j + 1] == '*'):
#                 pass
#             else:
#                 continue
#             if i + 2 <= dim - 1 and grid[i + 2][j] == '*':
#                 pass
#             else:
#                 continue
#             top_vertex.append((i, j))

# 嵌套循环 遍历矩阵的每一个元素

def find_top_of_rhombus(i, j, dim):
    # 行 左右列
    row = i
    left_column = j
    right_column = j
    # 存储每个点的坐标
    top_left = []
    top_right = []
    # 从顶点向左下方 向右下方
    for temp in range(dim):
        row = row + 1
        left_column = left_column - 1
        right_column = right_column + 1
        top_left.append((row, left_column))
        top_right.append((row, right_column))

    return top_left, top_right


# 判断元素是否越界 是否为 *
def check_element(top_left, top_right, dim, grid):
    # 菱形从大到小 倒着循环
    for temp in range(len(top_left) - 1, -1, -1):
        # 行 左右列
        row = top_left[temp][0]
        left_column = top_left[temp][1]
        right_column = top_right[temp][1]
        # 越界
        if (row >= dim or left_column < 0) or (row >= dim or right_column >= dim):
            top_left.pop(temp)
            top_right.pop(temp)
        # 没有 *
        # 处理 *** *** 中间为空？ 正向遍历 为空 切片
        # length = 0
        length = len(top_left)

    for temp in range(len(top_left)):
        # 找到为空的 较短的位置 确定菱形的左右顶点
        # 找到左边为空的位置
        if grid[top_left[temp][0]][top_left[temp][1]] != '*':
            length = temp - 1
            break
        # 找到右边为空的位置
        if grid[top_right[temp][0]][top_right[temp][1]] != '*':
            length = temp - 1
            break

    top_left = top_left[:length + 1]
    top_right = top_right[:length + 1]

    return top_left, top_right


def find_bottom_of_rhombus(i, top_left, top_right, dim, grid):
    # 判断是否找到底部了
    is_bottom = False
    # len(top_left)除去顶点外的长度 + 1 加上顶点 是这条边的长度 预期下顶点 2*len(top_left) + i
    l = len(top_left)
    for temp in range(l - 1, -1, -1):
        length = len(top_left)
        # 下顶点越界
        if 2 * length + i >= dim:
            # 返回左右列表的上一个找
            top_left.pop(temp)
            top_right.pop(temp)
        else:
            # 目标顶点 2 * length, j
            # 左顶点到下顶点遍历 看是否这条边都有 *
            # 右顶点到下顶点遍历 看是否这条边都有 *
            count = 1
            for _ in range(length - 1, -1, -1):
                new_row = top_left[temp][0] + count
                new_left_column = top_left[temp][1] + count
                new_right_column = top_right[temp][1] - count

                if new_row >= dim or new_left_column < 0 or new_left_column >= dim or \
                        new_right_column < 0 or new_right_column >= dim:
                    top_left.pop(temp)
                    top_right.pop(temp)
                    break

                if (grid[new_row][new_left_column] != '*') or (grid[new_row][new_right_column] != '*'):
                    top_left.pop(temp)
                    top_right.pop(temp)
                    break
                if (new_left_column == new_right_column) and grid[new_row][new_left_column] == '*':
                    is_bottom = True
                    break
                count += 1
        if is_bottom:
            break
    return top_left, top_right


# 确定菱形的各个坐标
def find_rhombus(i, j, top_left, top_right):
    rhombus = set()
    rhombus.add((i, j))
    length = len(top_left)
    bottom = (2 * length + i, j)
    # 处理上半部分菱形坐标
    for temp in range(length):

        row = top_left[temp][0]
        left_column = top_left[temp][1]
        right_column = top_right[temp][1]
        l = right_column - left_column
        count = left_column

        for temp2 in range(l + 1):
            rhombus.add((row, count))
            count += 1

    if not top_left:
        return set()

    row = top_left[length - 1][0] + 1
    left_column = top_left[length - 1][1] + 1
    right_column = top_right[length - 1][1] - 1
    l = right_column - left_column

    # 处理下半部分菱形坐标
    for temp in range(length):
        count = left_column
        for temp2 in range(l + 1):
            rhombus.add((row, count))
            count += 1

        row += 1
        left_column += 1
        right_column -= 1
        l = right_column - left_column

    return rhombus


# 遍历length的次数 向底部封口
# row = top_left[length - 1][0]
# left_column = top_left[length - 1][1]
# right_column = top_right[length - 1][1]
# for temp in range(len(top_left) - 1, -1, -1):
#     length = len(top_left)
#     count = 1
#     for temp2 in range(length - 1, -1, -1):
#         # 找左顶点的右下方
#         if grid[top_left[temp2][0] + count][top_left[temp2][1] + count] != '*':
#             pass
#         # 找右顶点的左下方
#         if grid[top_left[temp2][0] + count][top_right[temp2][1] - count] != '*':
#             pass
#         # 比较是否相交到下顶点
#         if top_left[temp2][1] + count == top_right[temp2][1] - count:
#             pass
# while True:
#     # 判断是否越界
#     if (i < dim - size and j - size >= 0 and grid[i + size][j - size] == '*') and \
#             (i < dim - size and j < dim - size and grid[i + size][j + size] == '*'):
#         size += 1
#     else:
#         break

set_list = []

for i in range(dim):
    for j in range(dim):
        # 顶点为 * 找菱形
        if grid[i][j] == '*':
            left, right = find_top_of_rhombus(i, j, dim)
            left, right = check_element(left, right, dim, grid)
            # print(i, j, left, right)
            left, right = find_bottom_of_rhombus(i, left, right, dim, grid)
            # print(i, j, left, right)
            rhombus = find_rhombus(i, j, left, right)
            # print(i, j, rhombus)
            if rhombus and len(left) > 0:
                if len(set_list) == 0:
                    set_list.append(rhombus)
                    results[len(left)].append((i, j))
                else:
                    # 如果是子集
                    if any(rhombus.issubset(subset) for subset in set_list):
                        pass
                    # 不是子集 符合
                    else:
                        set_list.append(rhombus)
                        results[len(left)].append((i, j))
            # 找到菱形最大的左右顶点所在的位置
            # while True:
            #     if (i < dim - size and j - size >= 0 and grid[i + size][j - size] == '*') and \
            #             (i < dim - size and j < dim - size and grid[i + size][j + size] == '*'):
            #         size += 1
            #     else:
            #         break
            # left = (i + size, j - size)
            # right = (i + size, j + size)
            # 开始收缩菱形
            # while True:
            #     # 东南方 和 西北方 都有 *
            #     if (i < dim - size and j < dim - size and grid[i + size + 1][j - size + 1] == '*') and \
            #             (i < dim - size and j - size >= 0 and grid[i + size + 1][j - size - 1] == '*'):
            #         # 继续东南和西北方封口
            #         size += 1
            #     # 没有的话退回上一行
            #     else:
            #         size -= 1
            #     # 行列相等 找到顶点
            #     if j - size + 1 == j - size - 1:
            #         results[size].append((i, j))
            #         break

print('Here are the rhombuses that are not included in any other:')
for size in sorted(results):
    print(f'Of size {size}:')
    for (i, j) in results[size]:
        print(f'  - with top vertex at location ({i}, {j})')
