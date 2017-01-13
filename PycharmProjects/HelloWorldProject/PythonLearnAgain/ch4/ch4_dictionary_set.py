def dict_testing():
    item = {'name': 'john'}
    items = dict(name='john')

    item[1, 2, 34] = "foo"  # this create a tyble 1,2,34 as key
    print('dictionary', item)


def set_testing():
    s = {1, 2, 3, 4, 5}
    t = {1, 2, 6}
    ss = {1, 2, 3, 4}
    print(s | t)
    print(s & t)
    print(s - t)
    print(s ^ t)

    forz = frozenset((1, 2, 3, 4))
    print(forz)

    print(ss.issubset(ss))


if __name__ == '__main__':
    dict_testing()
    set_testing()
