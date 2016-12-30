
def assi():
    print('sample')
    a=(1,2,3,4,(1,2))
    print(type(a),a)
    for f in a:
        print('value of f tuples',f,type(f))
        if tuple_check(f):
            for i in f:
                print('Printing sub tuple', i)


def tuple_check(f):
    if type(f) is tuple:return True
    else: return False



if __name__ == '__main__': assi()


