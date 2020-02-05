list = [0,1]
fn = int(input('geef een fn waarde: '))


def fibonacci(fn):
    for i in range(0, fn - 1):
        value = list[i] + list[i + 1]
        list.append(value)

    return list


print(fibonacci(fn))