
def test():
    buffersize = 50000

    filein = open('Bulk_data.txt','r')
    fileout =  open('Bulk_data_write.txt','w')

    buffer = filein.read(buffersize)
    print('length of buffer size outdie loop', len(buffer))
    while len(buffer):
        fileout.write(buffer)
        print('.')
        buffer = filein.read(buffersize)
        print('lenght of buffer insize', len(buffer))
    print('Done')

    # this will not work. you have to delete above line and try these line. Still not works perfect.
    for buf in file_read_iterable_generator(filein,buffersize):
        print('buf',len(buf))

def file_read_iterable_generator(filein,buffersize):
    buffer = filein.read(buffersize)
    yield buffer
    buffer = filein.read(buffersize)


def load_data():
    filein = open('Bulk_data.txt', 'w', encoding='utf_8')
    outbytes = bytearray()
    for i in range(128,10000):
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
    #load_data()