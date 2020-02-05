def move(ch, n):
    string = ch[n:] + ch[:n]
    print(string)
    return string


move('1011100', -3)
