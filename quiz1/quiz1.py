size = 10
print(f"Here is your coffee table of size {size}:")
print(' ' * 4 + ' ' + '-' * size)
print(' ' * 4 + '/|' + ' ' * (size - 2) + '/|')
print(' ' * 4 + '-' * size)
print(' ' * 4 + '|' + ' ' * (size - 2) + '|')
print()

num_dict = {'2': 'two', '3': 'three', '4': 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
char_dict = {'dashes': '-', 'stars': '*', 'carets': '^', 'dollars': '$'}

file_name = 'file.txt'

with open(file_name) as file:
    for line in file:
        if line.isspace():
            continue
        list = line.split()
        num1 = int(list[-2])
        num2 = num_dict[list[-2]]
        char1 = list[-1]
        char2 = char_dict[list[-1]]
        print(f"Here are your {num2} {char1}:")
        print(' ' * 4 + ' '.join(num1 * char2))
