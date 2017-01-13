def test_enumurate():
    li = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 0]

    for index, value in enumerate(li):  # this is same as an array of [ (0,value) , (1,value)]
        print(index, value)


if __name__ == '__main__':
    test_enumurate()
