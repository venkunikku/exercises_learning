def outer_fucntion():
    n = 0
    def inner_function():
        print('T-min %d' % n)
    while n <= 10:
        n += 1
        inner_function()


def nonlocal_tst():
    n =0
    def inner_function():
        nonlocal  n # not the nonlocal word here to access the outer nonlocal vairable.
        # In pythong2 you have to put the variable in a list or dict to access it inside inner functions
        n += 1
    while n <= 10:
        print(n)
        inner_function()

if __name__ == '__main__':
    #outer_fucntion()
    nonlocal_tst()