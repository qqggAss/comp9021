# Written by *** for COMP9021
#
# Prompts the user for the integers 0, 1... n, input
# in some order, for some natural number n,
# making up a list your_list,
# and for two integers, the second of which, say p,
# is between 0 and 10, to create a permutation of
# {0, ... p-1}, say my_list.
#
# Removes from your_list what is currently the smallest
# or largest element if it is curently the first or last
# element of the list, for as long as it can be done.
#
# Displays a picture that represents how to travel from
# 0 to p-1 in my_list, based on where they are located
# in the list.


from random import seed, shuffle
import sys

try:
    # split方法用户输入的字符串被分割成一个列表
    """
    列表推导式
    new_list = [expression for item in iterable if condition]
    expression：这是一个表达式，用于对每个元素执行操作，并将结果添加到新列表中。
    item：这是可迭代对象中的每个元素。
    iterable：这是可迭代对象，通常是一个列表、元组、集合或其他可迭代对象。
    condition（可选）：这是一个条件表达式，用于过滤可迭代对象中的元素。
    只有满足条件的元素才会被包括在新列表中。
    
    """
    your_list = [int(x) for x in
                 input('Enter a permutation of 0, ..., n '
                       'for some n >= 0: '
                       ).split()
                 ]
    # 检查用户输入的整数列表是否为空。如果为空，说明用户没有输入任何内容，将引发ValueError异常
    if not your_list:
        raise ValueError
    # set()将整数列表转换为集合，这是为了检查是否有重复的数字
    your_list_as_set = set(your_list)
    """
    条件检查排列是否包含了不同的整数，并且是否包含从0到n的所有整数（其中n是列表的长度）。
    如果条件不满足，说明排列不是有效的排列，将引发ValueError异常。
    反斜杠 \ 的作用是在代码换行时进行行连接。
    len(your_list_as_set) != len(your_list):
    集合没有重复元素 列表有的话 长度不等
    your_list_as_set != set(range(len(your_list))):
    创建一个包含从0到your_list长度减1的整数集合，这代表了一个标准的排列。
    
    """
    # 第二个判断可以判断是否从0输入 是否0-n都输入了(是否其中有数字没输入)
    if len(your_list_as_set) != len(your_list) \
            or your_list_as_set != set(range(len(your_list))):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

try:
    """
    生成器表达式:(expression for item in iterable if condition)
    expression：这是一个表达式，用于生成生成器的每个元素。
    item：这是可迭代对象中的每个元素。
    iterable：这是可迭代对象，通常是一个列表、元组、集合或其他可迭代对象。
    condition（可选）：这是一个条件表达式，用于筛选可迭代对象中的元素。
    只有满足条件的元素才会包括在生成器中。
    生成器表达式使用圆括号 () 来定义，并且可以在迭代中逐个生成元素，而不是一次性生成整个序列。
    生成器表达式是懒惰（lazy）的，它会逐个生成元素，而不是一次性生成整个列表。
    
    input(...)：使用input()函数提示用户输入文本，这里要求用户输入两个整数，用空格分隔。
    .split()：将用户输入的字符串按照空格分割成一个字符串列表。
    (int(x) for x in ...)：使用生成器表达式，
    将分割后的字符串列表中的每个元素 x 转换为整数，并创建一个包含两个整数的元组。
    for_seed, length = ...：将生成器表达式的结果解包，
    将其中的两个整数分别赋值给 for_seed 和 length 变量。
    
    """
    for_seed, length = \
        (int(x) for x in input('Enter two integers, '
                               'the second one between 0 and 10: '
                               ).split()
         )
    # 验证第二个整数是否在0到10的范围内
    if not 0 <= length <= 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
"""
seed() 是一个用于设置伪随机数生成器的种子（seed）的方法。
伪随机数生成器通常用于生成看似随机的数值序列，但实际上是通过一定的算法计算的，
因此在同样的种子下，它们会生成相同的数值序列，从而实现可复现性。

"""
seed(for_seed)
# 创建列表并打乱
my_list = list(range(length))
shuffle(my_list)

print('Here is your list:')
print('  ', your_list)
print('Here is my list:')
print('  ', my_list)

# INSERT THE FIRST PART OF YOUR CODE HERE

length = len(your_list)
max = len(your_list) - 1
min = 0

while your_list[0] == min or your_list[0] == max or \
        your_list[length - 1] == min or your_list[length - 1] == max:
    if your_list[0] == min or your_list[length - 1] == min:
        your_list.remove(min)
        min += 1
        length -= 1
    elif your_list[0] == max or your_list[length - 1] == max:
        your_list.remove(max)
        max -= 1
        length -= 1
    if length == 0:
        break

print()
print('Removing again and again the currently largest\n'
      'or smallest element in your list for as long as\n'
      'it currently starts or ends the list, we get:'
      )
print(your_list)
print()
print("That's how to travel in my list:")

# INSERT THE SECOND PART OF YOUR CODE HERE

for i in range(len(my_list)):
    index = my_list.index(i)
    if i == 0:
        print(index * ' ' + ' ' * index + f'{i}')
    else:
        gap = my_list.index(i) - my_list.index(i - 1)
        if gap < 0:
            gap = -gap
        if my_list.index(i) < my_list.index(i - 1):
            print(2 * index * ' ' + f'{i}' + 2 * gap * '-')
        else:
            space = my_list.index(i - 1)
            print(space * 2 * ' ' + gap * 2 * '-' + f'{i}')
