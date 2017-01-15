def outer_fucntion():
    n = 0
    def inner_function():
        print('T-min %d' % n)
    while n <= 10:
        n += 1
        inner_function()


def nonlocal_tst():
    n = 0
    def inner_function():
        nonlocal  n # not the nonlocal word here to access the outer nonlocal vairable.
        # In pythong2 you have to put the variable in a list or dict to access it inside inner functions
        #NOTE this is need only when you are trying to modify the variable outside the scope

        '''
        To alter this behavior, use the global statement. global simply
declares names as belonging to the global namespace, and it’s necessary only when
global variables will be modified. I

        '''
        '''
        Python 2 only allows variables to be reassigned in the innermost scope (local
variables) and the global namespace (using global).Therefore, an inner function can’t
reassign the value of a local variable defined in an outer function. For example, this
code does not work:

In Python 2, you can work around this by placing values you want to change in a list or
dictionary. In Python 3, you can declare n as nonlocal as follows:

        '''

        n += 1
    while n <= 10:
        print(n)
        inner_function()

def lexical_scoping():
    n = 100
    def inner_scoping():
        n += 1
        print('Inner values:',n)
    inner_scoping() #calling inner scope
    print('N outside:',n)


if __name__ == '__main__':
    outer_fucntion()
    nonlocal_tst()
    lexical_scoping()