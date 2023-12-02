# Written by *** for COMP9021
#
# Prompts the user for a ranking of the four horizontal and vertical
# directions, ⬆, ⮕, ⬇ and ⬅, from most preferred to least
# preferred, say d1, d2, d3 and d4.
#
# Determines the path that goes from a given point to another given
# point by following stars in a grid, provided that is possible,
# the path being uniquely defined by the following condition:
# to go from A to B,
# - if it is possible to start taking direction d1,
#   then the path from A to B starts by taking direction d1;
# - otherwise, if it is possible to start taking direction d2,
#   then the path from A to B starts by taking direction d2;
# - otherwise, if it is possible to start taking direction d3,
#   then the path from A to B starts taking direction d3;
# - otherwise, if it is possible to start taking direction d4,
#   then the path from A to B starts by taking direction d4.
#
# The grid and the path, if it exists, are output,
# - the endpoint of the path being represented by a red circle;
# - taking direction North being represented by a yellow square;
# - taking direction East being represented by a brown square;
# - taking direction South being represented by a green square;
# - taking direction West being represented by a purple square;
# - points not on the path being represented by black and white
#   squares depending on whether they are or not occupied by a star.
# (All these characters have been used in quiz 3.)
#
# Also outputs the length of the path, if it exists.

# ⮕⬅⬆⬇
# ⬅⮕⬆⬇   ⬆⮕⬇⬅  ⬇⬆⮕⬅   ⮕⬅⬇⬆

from random import seed, randrange
import sys

dim = 10


def display_grid():
    print('   ', '-' * (2 * dim + 1))
    for i in range(dim):
        print('   |', ' '.join('*' if grid[i][j] else ' '
                               for j in range(dim)
                               ), end=' |\n'
              )
    print('   ', '-' * (2 * dim + 1))


# print(chr(9899))  # 黑球
# print(chr(11036))  # 白方块
# print(chr(128308))  # 红球
# print(chr(128309))  # 蓝球
# print(chr(128999))  # 橙方块
# print(chr(129000))  # 黄方块
# print(chr(129001))  # 绿方块
# print(chr(129002))  # 紫方块
# print(chr(129003))  # 棕方块
# chr(11035) 黑方块

# 起点和终点坐标
def connect(start, end):
    # REPLACE PASS ABOVE WITH YOUR CODE
    # 字典存储上下左右和对应的坐标变化
    position_dict = {chr(11014): (-1, 0), chr(11015): (1, 0), chr(11013): (0, -1), chr(11157): (0, 1)}

    # 处理 起点或终点位置没有 * 的情况
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        print('There is no path joining both points.')
    else:
        # 用来记录访问过的坐标
        visited = set()
        # 用来记录路径
        path = [tuple(start)]

        find_way(start, end, grid, visited, path, dim, position_dict)

        color(path, grid)

        print(f'There is a path joining both points, of length {len(path)}:')

        # 通过行列索引更改元素 并输出
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = chr(11035)
                elif grid[i][j] == 0:
                    grid[i][j] = chr(11036)
                if j == 0:
                    print('    ' + f'{grid[i][j]}', end='')
                else:
                    print(grid[i][j], end='')
            print()


# POSSIBLY DEFINE OTHER FUNCTIONS


# 判断是否这个位置是否可以移动
def whether_can_move(position, grid, dim):
    row = position[0]
    column = position[1]
    if 0 <= row < dim and 0 <= column < dim and grid[row][column] == 1:  # '*':
        return True
    else:
        return False


# 寻路
def find_way(start, end, grid, visited, path, dim, position_dict):  # direction_preferences):
    # 找到终点
    if start == tuple(end):
        # path.append(start)
        return True
    row = start[0]
    column = start[1]
    # 添加到已经访问的集合中
    visited.add((row, column))
    # 用for循环处理各个优先级
    # for direction in direction_preferences:
    #     row_move, column_move = position_dict[direction]
    #     new_row = row + row_move
    #     new_column = column + column_move
    # 处理最高优先级的方向
    row_move, column_move = position_dict[direction_preferences[0]]
    new_row = row + row_move
    new_column = column + column_move
    # 判断移动的位置是否合法
    if (new_row, new_column) not in visited and whether_can_move((new_row, new_column), grid, dim):
        path.append((new_row, new_column))
        if find_way((new_row, new_column), end, grid, visited, path, dim, position_dict):  # , direction_preferences):
            return True
        else:
            # 如果没有路了 把这个坐标删掉
            path.pop()
    # 处理优先级第二的方向
    row_move, column_move = position_dict[direction_preferences[1]]
    new_row = row + row_move
    new_column = column + column_move
    # 判断移动的位置是否合法
    if (new_row, new_column) not in visited and whether_can_move((new_row, new_column), grid, dim):
        path.append((new_row, new_column))
        if find_way((new_row, new_column), end, grid, visited, path, dim, position_dict):  # , direction_preferences):
            return True
        else:
            path.pop()
    # 处理优先级第三的方向
    row_move, column_move = position_dict[direction_preferences[2]]
    new_row = row + row_move
    new_column = column + column_move
    # 判断移动的位置是否合法
    if (new_row, new_column) not in visited and whether_can_move((new_row, new_column), grid, dim):
        path.append((new_row, new_column))
        if find_way((new_row, new_column), end, grid, visited, path, dim, position_dict):  # , direction_preferences):
            return True
        else:
            path.pop()
    # 处理优先级第四的方向
    row_move, column_move = position_dict[direction_preferences[3]]
    new_row = row + row_move
    new_column = column + column_move
    # 判断移动的位置是否合法
    if (new_row, new_column) not in visited and whether_can_move((new_row, new_column), grid, dim):
        path.append((new_row, new_column))
        if find_way((new_row, new_column), end, grid, visited, path, dim, position_dict):  # , direction_preferences):
            return True
        else:
            path.pop()

    return False


# 获得从起点到终点的路径的列表
# def get_path(start, end, grid, dim, position_dict):  # , direction_preferences):
#     # 用来记录访问过的坐标
#     visited = set()
#     # 用来记录路径
#     path = [tuple(start)]
#     find_way(start, end, grid, visited, path, dim, position_dict)  # , direction_preferences)
#     return path


def color(path, grid):
    # 两个坐标得出移动方向 path[0] 到 path[1]   path[倒数第二个] 到 path[倒数第一个]  倒数第一个是红球
    length = len(path)
    for i in range(length - 1):
        # 这个点
        row = path[i][0]
        column = path[i][1]
        # 下个点
        next_row = path[i + 1][0]
        next_column = path[i + 1][1]
        # 判断移动的方向
        # 向北
        if next_row < row:
            grid[row][column] = chr(129000)
        # 向南
        if next_row > row:
            grid[row][column] = chr(129001)
        # 向西
        if next_column < column:
            grid[row][column] = chr(129002)
        # 向东
        if next_column > column:
            grid[row][column] = chr(129003)

    grid[path[-1][0]][path[-1][1]] = chr(128308)

    return grid


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
try:
    start = [int(x) for x in input('Enter coordinates '
                                   'of start point:'
                                   ).split()
             ]
    if len(start) != 2 or not (0 <= start[0] < dim) \
            or not (0 <= start[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    end = [int(x) for x in input('Enter coordinates '
                                 'of end point:'
                                 ).split()
           ]
    if len(end) != 2 or not (0 <= end[0] < dim) \
            or not (0 <= end[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
direction_preferences = input('Input the 4 directions, from most '
                              'preferred to least preferred:'
                              )
if set(direction_preferences) != {'⬆', '⮕', '⬇', '⬅'}:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
display_grid()
print()
connect(start, end)
