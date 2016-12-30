import copy
def shall_deep_copy_test():
    a = [1,2,[3,4]]

    # to make a shallow copy use the following

    b = list(a)
    print('b and a has same values now',b,'value of a: ',a)

    b.append(100)
    print('b has 1 more value but a is not changed', 'b:',b,'a:',a)

    # now modify something in that is copied from a
    b[2][0] = 500
    print('Value in a will be modified along with values in b now:','b:',b, 'a:', a)


    # Now making a deep copy
    # making a deep copy will not change the values in a when you modify in b

    c = copy._deepcopy(a)
    print('valye in c',c)


if __name__ == '__main__':
    shall_deep_copy_test()