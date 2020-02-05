message = input('Geef een tekst: ')
rotation = int(input('Geef een rotatie: '))


def caesar_cipher(message, rotation):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sch = ',.?!:'
    decription = ''
    for i in range(0, len(message)):
        character = message[i].upper()
        if character in letters:
            letter_index = letters.find(character)
            decription += letters[letter_index + rotation]
        else:
            if character in sch:
                ch_index = sch.find(character)
                decription += sch[ch_index]
            else:
                decription += ' '
    return decription


print(caesar_cipher(message, rotation))