file_name = 'file.txt'
new_file = open(file_name, 'w+')


def remove_spaces(file):
    with open(file, 'r') as f:
        new_lines = f.readlines()

    print(new_lines)

    for i in new_lines:
        new_file.write(i.lstrip())


# als test gebruik ik een andere python opdracht
remove_spaces('opdracht_6.py')
