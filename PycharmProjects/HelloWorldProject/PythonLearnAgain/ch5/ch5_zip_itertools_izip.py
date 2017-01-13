import itertools


def test_zip():
    key = ['name', 'last_name', 'sex']
    value = ['john', 'legendds', 'F']

    for k, v in zip(key, value):  # this is usually for fairly small list. This is not the best for later list.
        # this is ok in python3. the issue was in Python where you have to use itertools.izip for big lists
        print(k, v)


if __name__ == '__main__':
    test_zip()
