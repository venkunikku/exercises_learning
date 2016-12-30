
def test():
    print('hello')
    num=10j
    print(type(num))
    print('id',id(num))
    num=10
    print('id-change-num',id(num))
    num = 10j
    print('id-assignment back to old id',id(num))

    f = float()
    print(f)

if __name__ == '__main__':test()