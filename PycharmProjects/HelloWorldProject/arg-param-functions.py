
def test():
    call_another(1,2,10,20,30,40,50)


def call_another(one,two,*args):
    print(one,two)
    for i in args:
        print(i,end=' ')


if __name__ == '__main__':
    test()