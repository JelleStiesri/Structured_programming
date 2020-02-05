list = [1,5,8,9,6,2,2,4,5,6,-5,55,8,87,12,56]


def sort(list):
    for i in range(0, len(list) - 1):
        for x in range(0, len(list) - 1):
            if list[x] > list[x + 1]:
                key = list[x]
                list[x] = list[x + 1]
                list[x + 1] = key

    return list

print(sort(list))