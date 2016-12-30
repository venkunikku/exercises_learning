
def test():
    call_another(2,c=8)


def call_another(a,b=None,c=0):
    print(a,b,c)

if __name__ == '__main__':
    test()