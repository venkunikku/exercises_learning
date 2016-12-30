
def test():
    f = dict(

        one=1,
        two=2,
        thress=3,
        four=4
    )
    print(f['one'])
    print(f.get('onee','default value'))


if __name__ == '__main__':
    test()