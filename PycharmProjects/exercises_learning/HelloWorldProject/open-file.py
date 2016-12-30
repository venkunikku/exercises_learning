
def test():
    f = open('sample.txt')
    # print(type(f))
    # print(type(f.readlines()))
    for line in f.readlines():
        print(line,end='')
    f.close()

if __name__ == '__main__':
    test()