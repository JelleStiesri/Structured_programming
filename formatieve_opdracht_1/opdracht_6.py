list_1 = [5,5,5,8,9,5,4,1,2,3,5]
list_2 = [[1,5,8,6,8], [9,6,6,5,2,13,3,3], [5,6,6,4,7,8,9]]


def single_list(list):
    total_length = len(list)
    total_value = 0

    for i in list:
        total_value += i

    avg = total_value / total_length

    return round(avg, 2)


def multi_list(lists):
    avgs = []
    for list in lists:
        total_length = len(list)
        total_value = 0
        for x in list:
            total_value += x

        avg = total_value / total_length
        avgs.append(round(avg, 2))

    return avgs


print(single_list(list_1))
print(multi_list(list_2))
