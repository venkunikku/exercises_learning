#first 127 character of utf-8 has ascii


def test():
    try:
        filein = open('UTF8.txt', 'r', encoding='utf_8')
        fileout = open('utf8.html','w')
        outbytes =  bytearray() #mutable list of bytes.

        for line in filein: # gets the whole line
            # print(line,end='')
            for c in line: # get each character in the line
                if ord(c)> 127:
                    #print('String','this is what goes to {:04d}'.format(ord(c)))
                    #s = '{:04d}'.format(ord(c))
                    #print('bytes',s,'to',bytes(s,encoding='utf8'))
                    outbytes += bytes('&#{:04d};'.format(ord(c)),encoding='utf_8') #bytes is immutable object. bytes of HTML format string &#0356;
                else: outbytes.append(ord(c))
        convertedstring = str(outbytes,encoding='utf_8')

        print(convertedstring,file=fileout)
        print(convertedstring)


    finally:
        filein.close()


def all_chars():
    fo = open('char.txt', 'w')

    for i in range(5000):
        print(i, chr(i))
        fo.write(chr(i) + '\n')

    fo.close()

def write_chars():
    filein = open('UTF8.txt', 'a', encoding='utf_8')
    outbytes = bytearray()
    strng = None
    for i in range(3077,3200):
        outbytes += bytes(get_html_break(str(i)+'--Character of - {} \n'.format(chr(i))),encoding='utf_8')
    print('bytes',outbytes)
    bytesstr = str(outbytes,encoding='utf_8')
    print('bytest string',bytesstr)
    filein.write(bytesstr)
    filein.close()

def add_break_decorator(func):
    def add_decorator_inner(name):
        return '<br> {}'.format(func(name))
    return add_decorator_inner

@add_break_decorator
def get_html_break(text):
    return text




if __name__ == '__main__':
    test()
    #all_chars()
    #write_chars()
