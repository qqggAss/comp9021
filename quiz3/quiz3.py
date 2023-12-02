# Written by *** for COMP9021
#
# Implements a function that takes as argument a string
# consisting of arrows pointing North, East, South or West.
#
# Following the provided directions,
# - if the exploration gets back to the starting point, then this
#   common location will be represented by a black circle;
# - otherwise, the starting point will be represented by a blue circle
#   and the final destination by a red circle.

# All other visited locations will be represented by a square, of colour:
# - yellow if visited exactly once, 6 times, 11 times, 16 times...
# - orange if visited exactly twice, 7 times, 12 times, 17 times...
# - brown if visited exactly trice, 8 times, 13 times, 18 times...
# - green if visited exactly 4 times, 9 times, 14 times, 19 times...
# - purple if visited exactly 5 times, 10 times, 15 times, 20 times...

# The explored area is displayed within the smallest rectangle in
# which it fits; all unvisited locations within that rectangle are
# represented by white squares.
#
# The code points of the characters involved in this quiz are:
# 9899, 11036, 128308, 128309, 128999, 129000, 129001, 129002, 129003

# ⬆:11014
# ⬇:11015
# ⬅:11013
# ⮕:11157
# ord() 函数是一个Python内置函数，它用于返回表示一个字符的Unicode编码值（整数）
# chr() 函数是一个Python内置函数，用于将Unicode编码值（整数）转换为对应的字符。

# ('')
# ('⬆')
# ('⬆' + '⮕' * 3)
# ('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3)
# ('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3 + '⬆' + '⮕' * 2)
# (('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 2 + '⬆' + '⮕' * 2)
# (('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 3 + '⬆' + '⮕' * 2)
# (('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 4 + '⬆' + '⮕' * 2)
# (('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 5 + '⬆' + '⮕' * 2)
# (('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 6 + '⬆' + '⮕' * 2)
# ('⬅⬅⬆⬇⬅⬅⬇⬅')
# ('⬆⬆⬆⬇⮕⬇⬇⮕⬆⮕⬅⬅')
# ('⮕⮕⬇⬅⬆⬆⬅⬇⮕⮕⬅⬅⬅⮕⮕⮕⬅⬆⬆⮕')

# print(chr(9899))  # 黑球
# print(chr(11036))  # 白方
# print(chr(128308))  # 红球
# print(chr(128309))  # 蓝球
# print(chr(128999))  # 橙方
# print(chr(129000))  # 黄方
# print(chr(129001))  # 绿方
# print(chr(129002))  # 紫方
# print(chr(129003))  # 棕方


def explore_this_way(directions):
    x = 0
    y = 0
    x_max = 0
    x_min = 0
    y_max = 0
    y_min = 0
    point_dict = {}
    key = (x, y)
    point_dict[key] = 1
    length = len(directions)
    color_dict = {0: chr(129002), 1: chr(129000), 2: chr(128999), 3: chr(129003), 4: chr(129001)}
    for i in range(length):
        if directions[i] == chr(11014):
            y += 1
            key = (x, y)
            if key in point_dict:
                point_dict[key] += 1
            else:
                point_dict[(x, y)] = 1
            if y > y_max:
                y_max = y
            if y < y_min:
                y_min = y
        elif directions[i] == chr(11015):
            y -= 1
            key = (x, y)
            if key in point_dict:
                point_dict[key] += 1
            else:
                point_dict[(x, y)] = 1
            if y > y_max:
                y_max = y
            if y < y_min:
                y_min = y
        elif directions[i] == chr(11013):
            x -= 1
            key = (x, y)
            if key in point_dict:
                point_dict[key] += 1
            else:
                point_dict[(x, y)] = 1
            if x > x_max:
                x_max = x
            if x < x_min:
                x_min = x
        elif directions[i] == chr(11157):
            x += 1
            key = (x, y)
            if key in point_dict:
                point_dict[key] += 1
            else:
                point_dict[(x, y)] = 1
            if x > x_max:
                x_max = x
            if x < x_min:
                x_min = x
    finish_point = key
    if key == (0, 0):
        back_to_origin = True
    else:
        back_to_origin = False

    final_str = ''

    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            key = (x, y)
            if key == (0, 0):
                if back_to_origin:
                    final_str += chr(9899)
                else:
                    final_str += chr(128309)
                continue
            if key == finish_point:
                final_str += chr(128308)
                continue
            if key in point_dict:
                value = point_dict[key]
                if value % 5 == 0:
                    final_str += color_dict[0]
                elif value % 5 == 1:
                    final_str += color_dict[1]
                elif value % 5 == 2:
                    final_str += color_dict[2]
                elif value % 5 == 3:
                    final_str += color_dict[3]
                elif value % 5 == 4:
                    final_str += color_dict[4]
            else:
                final_str += chr(11036)
        if y != y_min:
            final_str += '\n'
    print(final_str)


# explore_this_way('')
# print()
# explore_this_way('⬆')
# print()
# explore_this_way('⬆' + '⮕' * 3)
# print()
# explore_this_way('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3)
# print()
# explore_this_way('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3 + '⬆' + '⮕' * 2)
# print()
# explore_this_way(('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 2 + '⬆' + '⮕' * 2)
# print()
# explore_this_way(('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 3 + '⬆' + '⮕' * 2)
# print()
# explore_this_way(('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 4 + '⬆' + '⮕' * 2)
# print()
# explore_this_way(('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 5 + '⬆' + '⮕' * 2)
# print()
# explore_this_way(('⬆' + '⮕' * 3 + '⬇' + '⬅' * 3) * 6 + '⬆' + '⮕' * 2)
# print()
# explore_this_way('⬅⬅⬆⬇⬅⬅⬇⬅')
# print()
# explore_this_way('⬆⬆⬆⬇⮕⬇⬇⮕⬆⮕⬅⬅')
# print()

explore_this_way('⮕⬅' * 1_000_000 + '⬆⬇⬆⬆')
