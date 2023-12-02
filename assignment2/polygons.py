# EDIT THE FILE WITH YOUR SOLUTION
import numpy as np


# 异常类
# class FileNotFoundError(Exception):
#     pass
class PolygonsError(Exception):
    pass


# 多边形类
class Polygons:
    def __init__(self, filename):

        # 存储该文件中所有的闭合路径
        self.polygons = []

        # 根据来源的方向确定的遍历的顺序
        self.order = {
            0: [5, 6, 7, 0, 1, 2, 3, 4],
            1: [6, 7, 0, 1, 2, 3, 4, 5],
            2: [7, 0, 1, 2, 3, 4, 5, 6],
            3: [0, 1, 2, 3, 4, 5, 6, 7],
            4: [1, 2, 3, 4, 5, 6, 7, 0],
            5: [2, 3, 4, 5, 6, 7, 0, 1],
            6: [3, 4, 5, 6, 7, 0, 1, 2],
            7: [4, 5, 6, 7, 0, 1, 2, 3]
        }
        # 遍历过的点的集合
        self.visited = set()

        try:
            with open(filename) as file:
                # 文本的内容存储到一个列表中
                self.grid = []
                # 遍历文件每一行
                for line in file:
                    # 文件中的某些行只包含空格字符，这些行经过 line.strip() 后变成了空字符串，
                    # 但由于它们不全是由 isspace() 检测的空白字符组成，
                    # 所以 if not line.isspace(): 判断为真，执行了下面的代码。
                    line = line.strip()
                    # 存每一行内容的列表
                    temp = []
                    # 如果这行不为空
                    # if not line.isspace():
                    # 遍历每一行的内容
                    for character in line:
                        if character not in ('0', '1', ' '):
                            raise PolygonsError('Incorrect input.')
                        elif character in ('0', '1'):
                            temp.append(character)
                    # temp 不为空 添加到 grid
                    if temp:
                        self.grid.append(temp)

                # 看行数是否符合要求 len(grid)
                if 2 <= len(self.grid) <= 50:
                    pass
                else:
                    raise PolygonsError('Incorrect input.')

                # 看列数是否符合要求
                length = len(self.grid[0])
                for i in range(len(self.grid)):
                    temp = len(self.grid[i])
                    if (2 <= temp <= 50) and (temp == length):
                        pass
                    else:
                        raise PolygonsError('Incorrect input.')
                    length = temp

        except FileNotFoundError:
            raise

        # polygon_list = self.find_polygons()
        # point_list = []
        # for i in range(len(polygon_list)):
        #     for j in range(len(polygon_list[i])):
        #         x = polygon_list[i][j][0]
        #         y = polygon_list[i][j][1]
        #         point_list.append((x, y))
        # temp = self.grid
        # for i in range(len(temp)):
        #     for j in range(len(temp[i])):
        #         if temp[i][j] == '1':
        #             if (i, j) in point_list:
        #                 pass
        #             else:
        #                 raise PolygonsError('Cannot get polygons as expected.')

    def find_first(self):
        # 找到开始时 1 的位置
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == '1' and (x, y) not in self.visited:
                    return x, y
        # 没有 1 的情况
        return None

    # 看是否可以移动
    def whether_can_move(self, x, y):
        # x y 最大值
        y_max = len(self.grid)
        x_max = len(self.grid[0])
        # 判断是否越界 是否为 1
        if 0 <= y < y_max and 0 <= x < x_max and self.grid[y][x] == '1':
            return True
        else:
            return False

    def clockwise_search(self, directions, direction_of_source, x, y):
        # 根据direction_of_source 确定开始搜索的方向
        # search_order = order[direction_of_source]
        # for i in range(len(search_order)):
        #     # 根据order找到的下一个寻找的顺序
        #     search_position = search_order[i]
        #     next_direction = directions[search_position]
        #     next_x = x + next_direction[0]
        #     next_y = y + next_direction[1]
        #     if self.whether_can_move(next_x, next_y):
        #         return next_x, next_y, search_position  # next_direction
        next_direction = directions[direction_of_source]
        next_x = x + next_direction[0]
        next_y = y + next_direction[1]
        if self.whether_can_move(next_x, next_y):
            return next_x, next_y, direction_of_source

        return None, None, None

    def find_next(self, x, y, direction_of_source):
        # 定义一个方向数组 北 东北 东 东南 南 西南 西 西北
        directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        # 根据方向的来源 找对应的方向 开始顺时针遍历
        # 从北开始 八个方向  0 1 2 3 4 5 6 7 对应 5 6 7 0 1 2 3 4
        # order = {
        #     0: [5, 6, 7, 0, 1, 2, 3, 4],
        #     1: [6, 7, 0, 1, 2, 3, 4, 5],
        #     2: [7, 0, 1, 2, 3, 4, 5, 6],
        #     3: [0, 1, 2, 3, 4, 5, 6, 7],
        #     4: [1, 2, 3, 4, 5, 6, 7, 0],
        #     5: [2, 3, 4, 5, 6, 7, 0, 1],
        #     6: [3, 4, 5, 6, 7, 0, 1, 2],
        #     7: [4, 5, 6, 7, 0, 1, 2, 3]
        # }
        return self.clockwise_search(directions, direction_of_source, x, y)

    def find_path(self):
        # 起点
        start_x, start_y = self.find_first()
        # 没有找到起点
        if start_x is None or start_y is None:
            return None
        start_point = (start_x, start_y)
        # 记录是否第一次访问起点
        # first_visit_start = True
        # 记录访问过的点
        # self.visited = set()
        # 记录路径的列表
        path = []
        # 遍历的顺序
        # self.order = {
        #     0: [5, 6, 7, 0, 1, 2, 3, 4],
        #     1: [6, 7, 0, 1, 2, 3, 4, 5],
        #     2: [7, 0, 1, 2, 3, 4, 5, 6],
        #     3: [0, 1, 2, 3, 4, 5, 6, 7],
        #     4: [1, 2, 3, 4, 5, 6, 7, 0],
        #     5: [2, 3, 4, 5, 6, 7, 0, 1],
        #     6: [3, 4, 5, 6, 7, 0, 1, 2],
        #     7: [4, 5, 6, 7, 0, 1, 2, 3]
        # }
        if self.dfs(start_x, start_y, start_point, path, self.visited, self.order, 3):
            return path
        else:
            return None

    # 深度优先搜索

    # def dfs(self, x, y, start_point, visited, first_visit_start, direction_of_source):
    #     # 起点在集合中 并且不是第一次访问
    #     # if (x, y) in visited:  # and first_visit_start is False:
    #     #     if x == start_point[0] and y == start_point[1] and not first_visit_start:
    #     #         return [(x, y)]
    #     #     return None
    #     # 如果当前点已经访问
    #     if (x, y) in visited:
    #         # 当前点是起点 而且不是第一次访问
    #         if x == start_point[0] and y == start_point[1] and not first_visit_start:
    #             return [(x, y)]
    #         else:
    #             return None
    #
    #     first_visit_start = False
    #
    #     # 添加到已经访问过的集合中
    #     visited.add((x, y))
    #
    #     if direction_of_source == 0:
    #         # 向北
    #         next_x, next_y, next_direction = self.find_next(x, y, 0)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 1:
    #         # 向东北
    #         next_x, next_y, next_direction = self.find_next(x, y, 1)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 2:
    #         # 向东
    #         next_x, next_y, next_direction = self.find_next(x, y, 2)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 3:
    #         # 向东南
    #         next_x, next_y, next_direction = self.find_next(x, y, 3)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 4:
    #         # 向南
    #         next_x, next_y, next_direction = self.find_next(x, y, 4)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 5:
    #         # 向西南
    #         next_x, next_y, next_direction = self.find_next(x, y, 5)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 6:
    #         # 向西
    #         next_x, next_y, next_direction = self.find_next(x, y, 6)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     if direction_of_source == 7:
    #         # 向西北
    #         next_x, next_y, next_direction = self.find_next(x, y, 7)
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             # 递归调用 深度优先搜索
    #             path = self.dfs(next_x, next_y, start_point, visited, first_visit_start, next_direction)
    #             # 如果有路径
    #             if path is not None:
    #                 return [(x, y)] + path
    #
    #     visited.remove((x, y))
    #     return None

    # def dfs(self, x, y, start_point, path, visited, direction_of_source):
    #     # 如果当前点已经访问
    #     # if (x, y) in visited:
    #     #     # 当前点是起点 而且不是第一次访问
    #     #     if x == start_point[0] and y == start_point[1] and not first_visit_start:
    #     #         path.append((x, y))
    #     #         return True
    #     #     else:
    #     #         return False
    #     # if not first_visit_start:
    #     # 添加到已经访问过的集合中
    #     visited.add((x, y))
    #
    #     # first_visit_start = False
    #
    #     if direction_of_source == 0:
    #         # 向北
    #         next_x, next_y, next_direction = self.find_next(x, y, 0)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 1:
    #         # 向东北
    #         next_x, next_y, next_direction = self.find_next(x, y, 1)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 2:
    #         # 向东
    #         next_x, next_y, next_direction = self.find_next(x, y, 2)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 3:
    #         # 向东南
    #         next_x, next_y, next_direction = self.find_next(x, y, 3)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 4:
    #         # 向南
    #         next_x, next_y, next_direction = self.find_next(x, y, 4)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 5:
    #         # 向西南
    #         next_x, next_y, next_direction = self.find_next(x, y, 5)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 6:
    #         # 向西
    #         next_x, next_y, next_direction = self.find_next(x, y, 6)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #
    #     if direction_of_source == 7:
    #         # 向西北
    #         next_x, next_y, next_direction = self.find_next(x, y, 7)
    #
    #         if (next_x, next_y) == start_point:
    #             path.append((next_x, next_y))
    #             return True
    #
    #         if (next_x, next_y) not in visited and next_x is not None and next_y is not None:
    #             path.append((next_x, next_y))
    #             # 递归调用 深度优先搜索
    #             if self.dfs(next_x, next_y, start_point, path, visited, next_direction):
    #                 return True
    #             else:
    #                 path.pop()
    #     # visited.remove((x, y))
    #     return False

    def dfs(self, x, y, start_point, path, visited, order, direction_of_source):

        if (x, y) in visited:
            return False

        self.visited.add((x, y))

        # 根据当前的点的来源的方向确定搜索的顺序
        search_order = self.order[direction_of_source]

        # 遍历所有可能的方向
        for i in range(len(search_order)):
            next_x, next_y, next_direction = self.find_next(x, y, search_order[i])

            if (next_x, next_y) == start_point:
                # 记录坐标点的同时记录一下方向 以便之后判断是否是顶点
                path.append((next_x, next_y, next_direction))

                return True

            if (next_x, next_y) not in self.visited and next_x is not None and next_y is not None:

                path.append((next_x, next_y, next_direction))

                if self.dfs(next_x, next_y, start_point, path, self.visited, self.order, next_direction):
                    return True
                path.pop()

        self.visited.remove((x, y))
        return False

    def find_polygons(self):
        # 所有找到的多边形路径
        # self.polygons = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == '1' and (x, y) not in self.visited:
                    start_point = (x, y)
                    path = self.find_path_from_start_point(start_point)
                    if path:
                        self.polygons.append(path)

        temp = []

        # 处理不构成多边形的情况 小于3个点 重复存储了顶点 所以是 >3
        for i in range(len(self.polygons)):
            if len(self.polygons[i]) > 3:
                temp.append(self.polygons[i])

        # 处理一条线的情况
        # for i in range(len(self.polygons)):
        #     for j in range(len(self.polygons[i]) - 1):
        #         pass

        self.polygons = temp

        return self.polygons

    def find_path_from_start_point(self, start_point):
        path = [(start_point[0], start_point[1], 3)]
        if self.dfs(start_point[0], start_point[1], start_point, path, self.visited, self.order, 3):
            return path
        return None

    def find_vertex(self):
        # 嵌套循环 处理 polygons 列表中的路径 找到顶点
        for i in range(len(self.polygons)):
            # 列表中最后一个点是原点 不用处理
            for j in range(len(self.polygons[i]) - 1):
                # 拿出元组中的值
                x = self.polygons[i][j][0]
                y = self.polygons[i][j][1]
                direction = self.polygons[i][j][-1]
                next_direction = self.polygons[i][j + 1][-1]
                if direction != next_direction:
                    is_vertex = 1
                    # 重新赋值 第三位表示是否是顶点
                    self.polygons[i][j] = (x, y, is_vertex)
                else:
                    is_vertex = 0
                    self.polygons[i][j] = (x, y, is_vertex)

            # 单独处理最后一位
            x = self.polygons[i][-1][0]
            y = self.polygons[i][-1][1]
            self.polygons[i][-1] = (x, y, 1)

            # 如果两个顶点是构不成多边形的 需要处理路径为一条线的情况

        return self.polygons

    # 计算周长
    def compute_perimeter(self):
        perimeter_list = []
        for i in range(len(self.polygons)):
            # 记录水平 垂直移动的数量
            horizontal_and_vertical = 0
            # 记录斜边的数量
            hypotenuse = 0
            for j in range(1, len(self.polygons[i])):
                last_x = self.polygons[i][j - 1][0]
                last_y = self.polygons[i][j - 1][1]
                current_x = self.polygons[i][j][0]
                current_y = self.polygons[i][j][1]
                # y轴移动
                if last_x == current_x and last_y != current_y:
                    horizontal_and_vertical += 1
                # x轴移动
                if last_x != current_x and last_y == current_y:
                    horizontal_and_vertical += 1
                # xy都移动 斜边
                if last_x != current_x and last_y != current_y:
                    hypotenuse += 1
            # Perimeter: a
            if horizontal_and_vertical != 0 and hypotenuse == 0:
                perimeter_list.append(round(horizontal_and_vertical * 0.4, 1))
            # Perimeter: a + b*sqrt(.32)
            if horizontal_and_vertical != 0 and hypotenuse != 0:
                perimeter_list.append(f'{round(horizontal_and_vertical * 0.4, 1)} + {hypotenuse}*sqrt(.32)')
            # Perimeter: b*sqrt(.32)
            if horizontal_and_vertical == 0 and hypotenuse != 0:
                perimeter_list.append(f'{hypotenuse}*sqrt(.32)')

        return perimeter_list

    # 计算面积
    def compute_area(self):
        area = []
        # 使用鞋带公式计算面积
        for i in range(len(self.polygons)):
            vertex = []
            for j in range(len(self.polygons[i])):
                # 将是顶点的坐标提取出来
                if self.polygons[i][j][-1] == 1:
                    vertex.append(self.polygons[i][j])
            first_part = 0
            second_part = 0
            for k in range(len(vertex)):
                # 将每个顶点的x坐标与其后一个顶点的y坐标相乘，计算这些乘积的和。
                # 将每个顶点的y坐标与其后一个顶点的x坐标相乘，也计算这些乘积的和。
                first_part += vertex[k][0] * vertex[(k + 1) % len(vertex)][1]
                second_part += vertex[k][1] * vertex[(k + 1) % len(vertex)][0]
            # area.append(round((abs(first_part - second_part) / 2) * (0.4 ** 2), 2))
            polygon_area = (abs(first_part - second_part) / 2) * (0.4 ** 2)
            format_area = f"{polygon_area:.2f}"
            area.append(format_area)

        return area

    # 计算凹凸性
    def compute_convex(self):
        # 通过向量计算凹凸性
        convex = []
        for i in range(len(self.polygons)):
            vertex = []
            for j in range(len(self.polygons[i])):
                # 将是顶点的坐标提取出来
                if self.polygons[i][j][-1] == 1:
                    vertex.append(self.polygons[i][j])
            # 遍历vertex
            # result 记录向量叉乘的结果
            result = 0
            # 假设多边形是凸的
            is_convex = True
            for k in range(len(vertex)):
                # 找到组成向量的两个点
                # 使用模运算确保索引不会超出列表的范围。
                # 从当前顶点 i 到下一个顶点 i+1 的向量。
                vector1 = (vertex[(k + 1) % len(vertex)][0] - vertex[k][0],
                           vertex[(k + 1) % len(vertex)][1] - vertex[k][1])
                # 从顶点 i+1 到顶点 i+2 的向量 k+1模运算防止越界
                vector2 = (vertex[(k + 2) % len(vertex)][0] - vertex[(k + 1) % len(vertex)][0],
                           vertex[(k + 2) % len(vertex)][1] - vertex[(k + 1) % len(vertex)][1])
                # 计算向量的叉乘
                compute = vector1[0] * vector2[1] - vector1[1] * vector2[0]
                # 存储第一次计算的叉乘结果
                if k == 0:
                    result = compute
                if (result < 0 and compute > 0) or (result > 0 and compute < 0):
                    convex.append('no')
                    # 此时是凹的
                    is_convex = False
                    break
            if is_convex:
                convex.append('yes')

        return convex

    # 计算不变的旋转的次数
    def compute_nb_of_invariant_rotations(self):
        # 记录旋转不变性
        # nb_of_invariant_rotations = []
        # 将grid转化为numpy数组
        # array = np.array(self.grid)
        # # 将多边形数据放入复制的网格
        # # 外部循环 处理每一条路径
        # for i in range(len(self.polygons)):
        #     # 处理新的路径时重新初始化复制的grid
        #     copy_array = np.zeros_like(array)
        #     # 具体到内部的一条路径
        #     for j in range(len(self.polygons[i])):
        #         # 将路径填充到copy_array中
        #         # 这里是反着来的 因为坐标系的关系
        #         copy_array[self.polygons[i][j][1], self.polygons[i][j][0]] = '1'
        #     # 进行旋转比较
        #     rotations = 0
        #     match = True
        #     for temp in range(4):
        #         rotations += 1
        #         # 使用90度旋转函数
        #         copy_array = np.rot90(copy_array)
        #
        #         # 判断是否可以旋转 用for循环遍历比较
        #         # for k in range(len(self.polygons[i])):
        #         #     if copy_array[self.polygons[i][k][1], self.polygons[i][k][0]] == '1':
        #         #         pass
        #         #     else:
        #         #         match = False
        #         #         break
        #
        #     if match:
        #         nb_of_invariant_rotations.append(rotations)
        #     else:
        #         nb_of_invariant_rotations.append(1)
        # 记录每个多边形的旋转不变性
        nb_of_invariant_rotations = []
        # 外层循环处理每一个多边形
        for i in range(len(self.polygons)):
            # 先对具体的一个多边形 求出他的坐标的最值
            x_record = []
            y_record = []
            for j in range(len(self.polygons[i])):
                x_record.append(self.polygons[i][j][0])
                y_record.append(self.polygons[i][j][1])
            # x y 的最值
            x_max = max(x_record)
            x_min = min(x_record)
            y_max = max(y_record)
            y_min = min(y_record)
            # 确定网格的尺寸
            grid_size = max(x_max - x_min, y_max - y_min) + 1
            # 生成网格
            array = np.zeros((grid_size, grid_size), dtype=int)

            # 在填充数组前调整坐标
            for j in range(len(self.polygons[i])):
                # 将路径填充到copy_array中
                # 这里是反着来的 因为坐标系的关系
                adjusted_x = self.polygons[i][j][0] - x_min
                adjusted_y = self.polygons[i][j][1] - y_min
                array[adjusted_y, adjusted_x] = 1

            copy_array = array

            rotations = 0

            for temp in range(4):
                # 使用90度旋转函数
                copy_array = np.rot90(copy_array)
                # 比较
                compare = np.array_equal(array, copy_array)
                if compare:
                    rotations += 1
                else:
                    pass

            nb_of_invariant_rotations.append(rotations)

        return nb_of_invariant_rotations

    # def compute_nb_of_invariant_rotations(self):
    #     nb_of_invariant_rotations = []
    #     # 对每一个多边形处理
    #     for i in range(len(self.polygons)):
    #         x = []
    #         y = []
    #         for j in range(len(self.polygons[i])):
    #             x.append(self.polygons[i][j][0])
    #             y.append(self.polygons[i][j][1])
    #             # 找多边形的中心
    #             x_center = float(sum(x) / len(x))
    #             y_center = float(sum(y) / len(y))
    #             xy = zip(x, y)
    #             # 初始化旋转类型发现标志
    #             find_rotations = [True, True, True]
    #             # 检查旋转
    #             for k in range(len(x)):
    #                 # 旋转90度
    #                 x_new = x_center - (y[k] - y_center)
    #                 y_new = y_center + (x[k] - x_center)
    #                 if (find_rotations[0]) and ((x_new, y_new) in xy):
    #                     pass
    #                 else:
    #                     find_rotations[0] = False
    #                 # 旋转180度
    #                 x_new = 2 * x_center - x[k]
    #                 y_new = 2 * y_center - y[k]
    #                 if (find_rotations[1]) and ((x_new, y_new) in xy):
    #                     pass
    #                 else:
    #                     find_rotations[1] = False
    #                 # 旋转270度
    #                 x_new = x_center + (y[k] - y_center)
    #                 y_new = y_center - (x[k] - x_center)
    #                 if (find_rotations[2]) and ((x_new, y_new) in xy):
    #                     pass
    #                 else:
    #                     find_rotations[2] = False
    #
    #             count = 0
    #             for l in range(len(find_rotations)):
    #                 if find_rotations[l] == True:
    #                     count += 1
    #
    #             nb_of_invariant_rotations.append(count + 1)
    #
    #     return nb_of_invariant_rotations

    # 计算多边形的深度
    def compute_depth(self):
        depth = []
        # 对原来的路径列表处理 去掉元组中的顶点
        path = []
        for i in range(len(self.polygons)):
            temp = []
            for j in range(len(self.polygons[i])):
                x = self.polygons[i][j][0]
                y = self.polygons[i][j][1]
                temp.append((x, y))
            path.append(temp)

        for i in range(len(path)):
            # 对每个多边形 取他的起点 左上角的点作为起始点
            point = (path[i][0])
            x = path[i][0][0]
            y = path[i][0][1]
            # 记录每一个
            depth_record = {}
            # 做一条延伸向左边边界的线 x轴坐标 -1 -1 -1...
            length = path[i][0][0] - 0
            # 处理在边界上的多边形
            if length == 0:
                depth.append(0)
            else:
                # 每到一个点 检查这个点是否在别的多边形路径中
                for j in range(length):
                    new_point = (x - 1, y)
                    known_x = new_point[0]
                    known_y = new_point[1]
                    count = 0
                    for k in range(len(path)):
                        polygon_path = path[k]
                        # 射线上的点是否与多边形有交点
                        if new_point in polygon_path:
                            # 找到这个点的vertex
                            vertex = 0
                            vertex_index = polygon_path.index(new_point)
                            prev_vertex = polygon_path[vertex_index - 1]
                            next_vertex = polygon_path[(vertex_index + 1) % len(polygon_path)]
                            # for x, y, z in self.polygons[k]:
                            #     if x == known_x and y == known_y:
                            #         vertex = z
                            #         break
                            vertex = self.polygons[k][vertex_index][-1]
                            # 交点事多边形的顶点 判定他的上下
                            if vertex == 1:
                                # 检查当前顶点是向上边还是向下边
                                if (prev_vertex[1] > new_point[1] and next_vertex[1] >= new_point[1]) or \
                                        (prev_vertex[1] >= new_point[1] and next_vertex[1] > new_point[1]):
                                    # 向上边
                                    count += 1
                                    depth_record[k] = count
                                # 否则为向下边，忽略不计
                            elif vertex == 0:
                                count += 1
                                depth_record[k] = count
                            # count += 1
                            # depth_record[k] = count
                    x -= 1
                count_depth = 0
                # 处理存储交点情况的字典
                for value in depth_record.values():
                    # 交点为奇数 被包含
                    if value % 2 != 0:
                        count_depth += 1
                depth.append(count_depth)

        return depth

    def analyse(self):
        self.find_polygons()
        self.find_vertex()
        # print(self.polygons)
        perimeter = self.compute_perimeter()
        area = self.compute_area()
        convex = self.compute_convex()
        rotation = self.compute_nb_of_invariant_rotations()
        depth = self.compute_depth()
        for i in range(len(self.polygons)):
            print(f'Polygon {i + 1}:')
            print(' ' * 4 + 'Perimeter: ' + f'{perimeter[i]}')
            print(' ' * 4 + 'Area: ' + f'{area[i]}')
            print(' ' * 4 + 'Convex: ' + f'{convex[i]}')
            print(' ' * 4 + 'Nb of invariant rotations: ' + f'{rotation[i]}')
            print(' ' * 4 + 'Depth: ' + f'{depth[i]}')

    def display(self):
        print(0)


# polys = Polygons('wrong_3.txt')
polys = Polygons('polys_2.txt')
# length = len(polys.grid)
# for i in range(length):
#     print(polys.grid[i], end='\n')

polys.analyse()
