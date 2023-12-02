# Implements a function that computes the maximum
# number of primes within a window of a given size,
# the first of which starts from a given lower bound
# and the last of which ends at a given upper bound.
# For all windows that achieve that maximum number
# within the window; outputs those two primes
# from smallest to largest first primes.
import time
from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


# You can assume that the function will be called with
# size a strictly positive integer,
# lower_bound an integer at least equal to 2, and
# upper_bound an integer at least equal to lower_bound.
# The function won't be tested for values of upper_bound
# greater than 10,000,000.
def primes_in_window(size, lower_bound, upper_bound):
    if size > upper_bound - lower_bound + 1:
        print('Window size is too large for these bounds,',
              'leaving it there.'
              )
        return
    # INSERT YOUR CODE HERE
    # 生成素数表
    sieve = sieve_of_primes_up_to(upper_bound)
    # 根据窗口设置左右指针
    left = lower_bound
    right = left + size - 1
    # 定义窗口内的素数的最值
    min_prime = 0
    max_prime = 0
    # 计算窗口中素数的个数 定义列表来存储
    count = 0
    count_in_each_window = []
    # 遍历第一个窗口
    for i in range(left, right + 1):
        # 找到素数 count计数+1 赋值给max
        if sieve[i]:
            count += 1
            max_prime = i
        # 序列是从小到大 再从头找最小的素数min
        for j in range(left, right + 1):
            if sieve[j]:
                min_prime = j
                break
    # 添加素数到列表里
    count_in_each_window.append(count)

    # 再使用一个列表存储每个窗口里素数到最值
    prime_list = [(min_prime, max_prime)]

    left += 1
    right = left + size - 1

    """
    把上面的代码放入while循环
    引入first_window_visited布尔变量来确保遍历第一个窗口的代码只在第一次进入while循环时执行一次。
    或
    for i in range(left, upper_bound - size + 2):
    if i == left:  # 第一次循环，处理第一个窗口
    else:
    """

    while right <= upper_bound:
        if size == 1:
            if sieve[left]:
                min_prime = left
                max_prime = left
                # 这里要处理count ！！！
                count = 1
            else:
                count = 0
        else:
            # if sieve[left - 1]:
            #     count -= 1
            #     for i in range(left, right + 1):
            #         if sieve[i]:
            #             min_prime = i
            #             break
            # else:
            #     # 走的数字不是素数也要处理 ！！！
            #     for i in range(left, right + 1):
            #         if sieve[i]:
            #             min_prime = i
            #             break
            for i in range(left, right + 1):
                if sieve[i]:
                    min_prime = i
                    break
            if sieve[left - 1]:
                count -= 1
            if sieve[right]:
                count += 1
                max_prime = right
            else:
                for j in range(right, left - 1, -1):
                    if sieve[j]:
                        max_prime = j
                        break
        prime_list.append((min_prime, max_prime))
        count_in_each_window.append(count)
        left += 1
        right = left + size - 1

    max_prime_numbers = max(count_in_each_window)
    numbers_of_windows = count_in_each_window.count(max_prime_numbers)

    if max_prime_numbers:
        if size == 1:
            print(f'There is at most one prime in a window of size {size}.')
        else:
            # 注意这里 at most one ！！！
            if max_prime_numbers == 1:
                print(f'There are at most one primes in a window of size {size}.')
            else:
                print(f'There are at most {max_prime_numbers} primes in a window of size {size}.')
        previous = None
        for i in range(len(count_in_each_window)):
            if count_in_each_window[i] == max_prime_numbers:
                (x, y) = prime_list[i]
                current = (x, y)
                if current != previous:
                    print(f'In some window, the smallest prime is {x} and the largest one is {y}.')
                previous = current
    else:
        print(f'There is no prime in a window of size {size}.')


# primes_in_window(1, 8_999_999, 9_000_100)
# primes_in_window(2, 123_456, 123_987)
# primes_in_window(3, 300_000, 300_300)
primes_in_window(6, 1_000_000, 1_000_500)
