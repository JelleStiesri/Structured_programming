first = input('enter line: ')
second = input('enter second line: ')

def check_index(first, second):
    if len(first) > len(second):
        length = len(second)

    else:
        length = len(first)


    for i in range(0, length - 1):
        if first[i] != second[i]:
            print('wrong at', i)
            break



check_index(first, second)
