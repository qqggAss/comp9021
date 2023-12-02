# Will be tested with year between 1913 and 2013.


import csv


def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', \
        'Sep', 'Oct', 'Nov', 'Dec'
    # INSERT YOUR CODE HERE
    record = []
    result = []
    with open('cpiai.csv') as file:

        max = -10000

        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'Date':
                pass
            else:
                if row[0][:4] == str(year):
                    if float(row[-1]) >= float(max):
                        max = row[-1]
                    record.append(row)

        # for line in file:
        #     line = line.strip()
        #     temp = line.split(',')
        #     if temp[0] == 'Date':
        #         pass
        #     else:
        #         if temp[0][:4] == str(year):
        #             if float(temp[-1]) >= float(max):
        #                 max = temp[-1]
        #             record.append(temp)

    month_record = []
    for i in range(len(record)):
        if float(record[i][-1]) == float(max):
            mon = int(record[i][0][5:7]) - 1
            month_record.append(months[mon])
    month_record = ', '.join(month_record)
    print(f'In {year}, maximum inflation was: {max}')
    print(f'It was achieved in the following months: {month_record}')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
