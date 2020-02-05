import random


def num_guess():
    num = random.randint(1,20)
    print(num)

    while True:
        guess = int(input('Geef een getal tussen 1 en 20: '))
        if guess == num:
            return 'Goed geraden'
        else:
            print('fout')


print(num_guess())