def selfmade_palindroom(word):
    reversed = word[::-1]
    if reversed == word:
        return 'palindroom'
    else:
        return 'geen palindroom'


def library_palindroom(word):
    reverse = ''.join(reversed(word))
    if reverse == word:
        return 'palindroom'
    else:
        return 'geen palindroom'


print(selfmade_palindroom('racecar'))
print(library_palindroom('racecar'))