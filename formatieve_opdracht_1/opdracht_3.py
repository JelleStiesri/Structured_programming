list_1 = [1,2,5,5,8,1,5,2,5,8,44,6,5,12,5,1,6,6,6,8,7,8,8,8,9,9]
list_2 = [1,5,6,8,12,3,6,8,5,5,7]
list_3 = [0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]

# 3a
def count(value, lst):
    if not type(value) == int:
        return 'vul een heel nummer in'
    else:
        if value in lst:
            count = lst.count(value)
            return count
        else:
            return 'getal niet in de lijst'

# 3b
def difference():
    for i in range(0, len(list_2) - 1):
        if list_2[i] >= list_2[i + 1]:
            difference = list_2[i] - list_2[i + 1]
        else:
            difference = list_2[i + 1] - list_2[i]

        print('verschil: ', difference)

# 3c
def check():
    zero_count = count(0, list_3)
    one_count = count(1, list_3)

    if zero_count > one_count:
        return 'Er zijn meer nullen dan enen'
    elif zero_count > 12:
        return 'Er zijn teveel nullen'
    else:
        return 'lijst goedgekeurd'


print(count(5, list_1))
difference()
print(check())
