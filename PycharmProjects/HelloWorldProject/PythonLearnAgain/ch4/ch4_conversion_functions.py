def conversion_fucntions():
    x = '77'
    y = 'this is a string'

    print(int(x, 10))

    print('Ordinal', ord('a'))
    print('Hexadecimal', hex(97))
    print('Binary', bin(97))
    print('Octal', oct(97))

    a = tuple((1, 2, 3, 4))
    b = 1
    if a and b:
        print('True')
    else:
        print("False")


if __name__ == '__main__':
    conversion_fucntions()
