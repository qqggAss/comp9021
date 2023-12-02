# EDIT THE FILE WITH YOUR SOLUTION

# 把文件的内容存储到一个列表中
def generate_text_list(file_name):
    with open(file_name) as file:
        # 文本的内容存储到一个列表中
        text_list = []
        for line in file:
            # text_list += line.split()
            text_list.extend(line.split())

    return text_list


def remove_and_record(text_list):
    # 记录每句话开始和结束的下标索引
    end_list = []
    # 存储引号的位置
    quote = []

    for i in range(len(text_list)):

        # 处理列表中每个元素的末尾的逗号或者冒号(如果有) 移除
        # if text_list[i].endswith('?'):
        if (text_list[i][-1] == ',') or (text_list[i][-1] == ':'):
            # sequence[start:end:step] 切片操作 类似range
            text_list[i] = text_list[i][:-1]

        if text_list[i][-2:] == ',"':
            temp = text_list[i]
            temp = temp[:-2] + temp[-1]
            text_list[i] = temp

        # if (text_list[i][-1] == '.') or (text_list[i][-1] == '!') \
        #         or (text_list[i][-1] == '?') or (text_list[i][-2:] == '."') \
        #         or (text_list[i][-2:] == '?"') or (text_list[i][-2:] == '!"'):
        #     end_list.append(i)

        # 处理每句话的末尾
        if (text_list[i][-1] == '.') or (text_list[i][-1] == '!') or (text_list[i][-1] == '?'):
            end_list.append(i)
            # 处理掉末尾的标点
            text_list[i] = text_list[i][:-1]

        if (text_list[i][-2:] == '."') or (text_list[i][-2:] == '!"') or (text_list[i][-2:] == '?"'):
            end_list.append(i)
            # 处理掉双引号左边的标点
            # 包含字符串的列表，不可以直接使用切片和字符串连接
            # 先合并再更新
            temp = text_list[i]
            temp = temp[:-2] + temp[-1]
            text_list[i] = temp

        # 处理引号
        if text_list[i][0] == '"':
            quote.append(i)
            text_list[i] = text_list[i][1:]
        if text_list[i][-1] == '"':
            quote.append(i)
            text_list[i] = text_list[i][:-1]

    return text_list, end_list, quote


# 移除列表中元素的逗号和冒号
# def remove_commas_colons(text_list):
#     # 处理列表每个元素中末尾的逗号(如果有) 冒号去掉
#     for i in range(len(text_list)):
#         # if text_list[i].endswith('?'):
#         if (text_list[i][-1] == ',') or (text_list[i][-1] == ':'):
#             # sequence[start:end:step] 切片操作 类似range
#             text_list[i] = text_list[i][:-1]
#
#         if text_list[i][-2:] == ',"':
#             temp = text_list[i]
#             temp = temp[:-2] + temp[-1]
#             text_list[i] = temp
#
#     return text_list


# 记录每个句子结束位置的索引 确定之后去除 . ! ?
# def record_end_of_sentences(text_list):
#     # 记录每句话开始和结束的下标索引
#     end_list = []
#     for i in range(len(text_list)):
#         # if (text_list[i][-1] == '.') or (text_list[i][-1] == '!') \
#         #         or (text_list[i][-1] == '?') or (text_list[i][-2:] == '."') \
#         #         or (text_list[i][-2:] == '?"') or (text_list[i][-2:] == '!"'):
#         #     end_list.append(i)
#
#         if (text_list[i][-1] == '.') or (text_list[i][-1] == '!') or (text_list[i][-1] == '?'):
#             end_list.append(i)
#             # 处理掉末尾的标点
#             text_list[i] = text_list[i][:-1]
#
#         if (text_list[i][-2:] == '."') or (text_list[i][-2:] == '!"') or (text_list[i][-2:] == '?"'):
#             end_list.append(i)
#             # 处理掉双引号左边的标点
#             # 包含字符串的列表，不可以直接使用切片和字符串连接
#             # 先合并再更新
#             temp = text_list[i]
#             temp = temp[:-2] + temp[-1]
#             text_list[i] = temp
#
#     return end_list, text_list


# 确定句子的末尾的索引之后去除 . ! ?
# def remove_end_punctuations(text_list):
#     for i in range(len(text_list)):
#         if (text_list[i][-1] == '.') or (text_list[i][-1] == '!') \
#                 or (text_list[i][-1] == '?'):
#             # 处理掉末尾的标点
#             text_list[i] = text_list[i][:-1]
#
#         if (text_list[i][-2:] == '."') or (text_list[i][-2:] == '!"') \
#                 or (text_list[i][-2:] == '?"'):
#             # 处理掉双引号左边的标点
#             # 包含字符串的列表，不可以直接使用切片和字符串连接
#             # 先合并再更新
#             temp = text_list[i]
#             temp = temp[:-2] + temp[-1]
#             text_list[i] = temp
#
#     return text_list


# 处理引号
# def deal_double_quote(text_list):
#     # 存储引号的位置
#     quote = []
#     for i in range(len(text_list)):
#         if text_list[i][0] == '"':
#             quote.append(i)
#             text_list[i] = text_list[i][1:]
#         if text_list[i][-1] == '"':
#             quote.append(i)
#             text_list[i] = text_list[i][:-1]
#
#     return quote


# 找名字
def find_name(text_list, end_list):
    # 记录现在是第几句话
    count = 0
    # 定义集合存储名字
    name_set = set()
    for i in range(len(text_list)):
        # 记录现在是第几句话
        if i > end_list[count]:
            count += 1
        # 找单个的Sir
        if text_list[i] == 'Sir':
            name_set.add(text_list[i + 1])
        # 找多个的Sirs
        if text_list[i] == 'Sirs':
            for j in range(i + 1, end_list[count] + 1):

                if text_list[j] == 'and':
                    if text_list[j + 1] == 'I':
                        break
                    else:
                        name_set.add(text_list[j + 1])
                        break
                else:
                    if text_list[j] == 'I':
                        continue
                    else:
                        name_set.add(text_list[j])

                # if text_list[j] != 'and':
                #     name_set.add(text_list[j])
                # else:
                #     name_set.add(text_list[j + 1])
        # # 记录现在是第几句话
        # if i > end_list[count]:
        #     count += 1
    name_list = sorted(name_set)

    return name_list


# 找到谁说了话和说话的内容
def find_who_and_speak(text_list, quote_list, end_list):
    quote_index = 1
    # 存储谁在说话
    who_list = []
    # 存储说的内容
    speak_list = []
    # 一共几句话，进行几次循环，每次循环在第i句话内找说话的名字和内容
    for i in range(len(end_list)):
        # 通过引号和句末的位置找是在第几句有说话的内容
        if quote_list[quote_index] > end_list[i]:
            continue
        # 找到说话的内容
        else:
            temp = []
            # 单独处理如果骑士在第一句就说话
            if i == 0:
                for j in range(end_list[0] + 1):
                    if j < quote_list[quote_index - 1]:
                        if text_list[j] == 'Sir':
                            who_list.append(text_list[j + 1])
                    elif (j >= quote_list[quote_index - 1]) and (j <= quote_list[quote_index]):
                        temp.append(text_list[j])
                    elif j > quote_list[quote_index]:
                        if text_list[j] == 'Sir':
                            who_list.append(text_list[j + 1])
            else:
                for j in range(end_list[i - 1] + 1, end_list[i] + 1):
                    if j < quote_list[quote_index - 1]:
                        if text_list[j] == 'Sir':
                            who_list.append(text_list[j + 1])
                    elif (j >= quote_list[quote_index - 1]) and (j <= quote_list[quote_index]):
                        temp.append(text_list[j])
                    elif j > quote_list[quote_index]:
                        if text_list[j] == 'Sir':
                            who_list.append(text_list[j + 1])
            speak_list.append(temp)
            quote_index += 2
            if quote_index > quote_list.index(quote_list[-1]):
                break

    return who_list, speak_list


# 根据所有的sir生成所有的可能性
def generate_all_possibilities(name_list):
    # 生成所有的情况
    length = len(name_list)
    all_possibilities = [f'{i:0{length}b}' for i in range(2 ** length)]

    return all_possibilities


# 处理说的话
# 骑士说真话 所以如果一个人是骑士 那么他说的话要成立
# 无赖说假话 所以如果一个人是无赖 那么他说的话不能成立

# 处理 conjunction_of_sirs 这种形式
def deal_conjunction(who_is_speaking, sentence, speak_names, name_list):
    for i in range(len(sentence)):
        if sentence[i] == 'Sir':
            speak_names.append(sentence[i + 1])
        elif sentence[i] == 'I':
            speak_names.append(who_is_speaking)
        elif sentence[i] == 'us':
            speak_names = name_list

    return speak_names


# case用来确定当前处理的是哪种类型的句子 identity用来处理句子末尾是knight还是knave
def filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names, identity):
    # 复制一个列表 对这个复制列表进行操作 不影响遍历
    copy_list = list(all_possibilities)
    # 遍历所有的可能性
    for possibility in all_possibilities:
        # 在所有情况中找到现在说话的sir的身份是 0 还是 1
        identity_of_speaker = possibility[name_list.index(who_is_speaking)]
        # 说话的sir的身份是 1 骑士 骑士只说真话 conjunction of sirs 至少有一个是骑士 成立
        if identity_of_speaker == '1':
            is_true = 0
            # 遍历说的话中的sir的身份
            for i in speak_names:
                # 判断在当前这种可能的情况下 这个sir的身份是什么
                value = possibility[name_list.index(i)]
                # 如果是 identity == 1 骑士 统计数量 identity == 0 无赖 统计数量
                if value == identity:
                    is_true += 1
            if case == 1:
                # 满足 At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
                if is_true >= 1:
                    # 保留这一种可能
                    pass
                else:
                    # 移除这一种可能
                    copy_list.remove(possibility)
            if case == 2:
                # 满足 At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
                if is_true <= 1:
                    pass
                else:
                    copy_list.remove(possibility)
            if case == 3:
                # 满足Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
                if is_true == 1:
                    pass
                else:
                    copy_list.remove(possibility)
            if case == 4:
                # 满足All/all of us are Knights/Knaves
                if is_true == len(speak_names):
                    pass
                else:
                    copy_list.remove(possibility)
            if case == 5:
                # 满足I am a Knight/Knave
                if (is_true == 1) and (possibility[name_list.index(speak_names[0])]):
                    pass
                else:
                    copy_list.remove(possibility)
            if case == 6:
                # Sir Sir_Name is a Knight/Knave
                if (is_true == 1) and (possibility[name_list.index(speak_names[0])]):
                    pass
                else:
                    copy_list.remove(possibility)
            if case == 7:
                # Disjunction_of_Sirs is a Knight/Knave or
                if is_true >= 1:
                    pass
                else:
                    copy_list.remove(possibility)
            if case == 8:
                pass
                # Conjunction_of_Sirs are Knights/Knaves
                if is_true == len(speak_names):
                    pass
                else:
                    copy_list.remove(possibility)

        # 说话的sir的身份是 0 无赖 说假话 conjunction of sirs 至少有一个是骑士 这句话是不成立的
        else:
            is_true = 0
            for i in speak_names:
                value = possibility[name_list.index(i)]
                # 还是找真话 但是是删除 不是保留
                if value == identity:
                    is_true += 1
            if case == 1:
                # 满足at least
                if is_true >= 1:
                    # 移除这一种可能
                    copy_list.remove(possibility)
                else:
                    # 保留
                    pass
            if case == 2:
                if is_true <= 1:
                    copy_list.remove(possibility)
                else:
                    pass
            if case == 3:
                if is_true == 1:
                    copy_list.remove(possibility)
                else:
                    pass
            if case == 4:
                if is_true == len(speak_names):
                    copy_list.remove(possibility)
                else:
                    pass
            if case == 5:
                # 满足I am a Knight/Knave
                if (is_true == 1) and (possibility[name_list.index(speak_names[0])]):
                    copy_list.remove(possibility)
                else:
                    pass
            if case == 6:
                # Sir Sir_Name is a Knight/Knave
                if (is_true == 1) and (possibility[name_list.index(speak_names[0])]):
                    copy_list.remove(possibility)
                else:
                    pass
            if case == 7:
                # Disjunction_of_Sirs is a Knight/Knave or
                if is_true >= 1:
                    copy_list.remove(possibility)
                else:
                    pass
            if case == 8:
                # Conjunction_of_Sirs are Knights/Knaves
                if is_true == len(speak_names):
                    copy_list.remove(possibility)
                else:
                    pass

    all_possibilities = copy_list

    return all_possibilities


def deal_speak(who_list, speak_list, name_list, all_possibilities):
    count = 0
    for sentence in speak_list:
        who_is_speaking = who_list[count]
        # print('说话的是', who_is_speaking)
        speak_names = []

        # 处理At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
        if ((sentence[0] == 'at') or (sentence[0] == 'At')) and (sentence[1] == 'least'):
            # 标记
            case = 1
            # 找到说的话中涉及到的名字
            speak_names = deal_conjunction(who_is_speaking, sentence, speak_names, name_list)
            # print(speak_names)
            # 话中身份为骑士 句末
            if sentence[-1] == 'Knight':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

            # 话中身份为无赖
            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
        elif ((sentence[0] == 'at') or (sentence[0] == 'At')) and (sentence[1] == 'most'):
            case = 2
            speak_names = deal_conjunction(who_is_speaking, sentence, speak_names, name_list)
            # print(speak_names)

            # 话中身份为骑士
            if sentence[-1] == 'Knight':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
        elif (sentence[0] == 'exactly') or (sentence[0] == 'Exactly'):
            case = 3
            speak_names = deal_conjunction(who_is_speaking, sentence, speak_names, name_list)
            # print(speak_names)

            # 话中的身份为骑士
            if sentence[-1] == 'Knight':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理All/all of us are Knights/Knaves
        elif (sentence[0] == 'all') or (sentence[0] == 'All'):
            case = 4
            speak_names = name_list
            # print(speak_names)
            if sentence[-1] == 'Knights':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)
            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理I am a Knight/Knave
        elif (sentence[0] == 'I') and (sentence[1] == 'am'):
            case = 5
            speak_names.append(who_is_speaking)
            # print(speak_names)
            if sentence[-1] == 'Knight':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)
            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理Sir Sir_Name is a Knight/Knave
        elif (sentence[0] == 'Sir') and (sentence[2] == 'is'):
            case = 6
            speak_names.append(sentence[1])
            # print(speak_names)
            if sentence[-1] == 'Knight':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)
            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理Disjunction_of_Sirs is a Knight/Knave
        elif ((sentence[0] == 'I') or (sentence[0] == 'Sir')) and (
                (sentence[-1] == 'Knight') or (sentence[-1] == 'Knave')):
            case = 7
            # 处理方法和conjunction相同
            speak_names = deal_conjunction(who_is_speaking, sentence, speak_names, name_list)
            # print(speak_names)
            if sentence[-1] == 'Knight':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)
            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 处理Conjunction_of_Sirs are Knights/Knaves
        elif ((sentence[0] == 'I') or (sentence[0] == 'Sir')) and (
                (sentence[-1] == 'Knights') or (sentence[-1] == 'Knaves')):
            case = 8
            speak_names = deal_conjunction(who_is_speaking, sentence, speak_names, name_list)
            # print(speak_names)
            if sentence[-1] == 'Knights':
                identity = '1'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)
            else:
                identity = '0'
                all_possibilities = filter_possibility(case, all_possibilities, name_list, who_is_speaking, speak_names,
                                                       identity)

        # 这句话处理结束 进入下一句话
        count += 1

    return all_possibilities


def show_result(name_list, all_possibilities):
    sirs = 'The Sirs are: ' + ' '.join(name_list)
    print(sirs)

    if len(all_possibilities) == 0:
        print('There is no solution.')
    else:
        if len(all_possibilities) == 1:
            print('There is a unique solution:')
            for name in name_list:
                if all_possibilities[0][name_list.index(name)] == '1':
                    print(f'Sir {name} is a Knight.')
                else:
                    print(f'Sir {name} is a Knave.')
        else:
            print(f'There are {len(all_possibilities)} solutions.')


def main():
    # file_name = 'test_5.txt'

    file_name = input('Which text file do you want to use for the puzzle? ')

    text = generate_text_list(file_name)

    # text = remove_commas_colons(text)
    #
    # end, text = record_end_of_sentences(text)
    #
    # # text = remove_end_punctuations(text)
    #
    # quote = deal_double_quote(text)

    text, end, quote = remove_and_record(text)

    name = find_name(text, end)

    # 是否存在没有人说话的情况
    # quote不为空 有人说话
    if quote:

        who, speak = find_who_and_speak(text, quote, end)

        all_possibilities = generate_all_possibilities(name)

        all_possibilities = deal_speak(who, speak, name, all_possibilities)

    # quote为空 没有人说话
    else:

        all_possibilities = generate_all_possibilities(name)

    show_result(name, all_possibilities)


main()
