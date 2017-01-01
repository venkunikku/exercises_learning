
def test():
    print(b'\xc3\xb6')
    print(b'\xc3\xb6'.decode('utf-8'))
    #print(s)
    #print(s.decode('utf-8'))
    print(u'\u00f6')
    s = u'this is one more way to enter unicode chars \N{LATIN SMALL LETTER O WITH DIAERESIS}'
    ss = u'this is one more way to enter unicode chars \u00f6'
    print(s)
    print(u'\u2A14')
    print(u'\u2514\u2510')

    # this is not allowed. A r with single slash is not allowed
    #print(r'\')

    print(r'\u2A14')

    import sys
    print(sys.getsizeof(s))
    print(sys.getsizeof(ss))
    print(len('111111111111111111111111111111111111111111111111111111111111111'))

    print(bytes('hello'.encode('utf-8')))

    w = 'Hello World !!'
    for l in w:
        #print(':'.join('{:02x}'.format(ord(l))),end=' ')
        # 'x' convert to hex
        print('{:02x}'.format(ord(l)))

    #converting to hex
        print('Hex values:',hex(ord(l)))


if __name__ == '__main__':
    test()