
def test():
    try:
        # f = open('samp.txt')
        print(call_another(1,0))
    except IOError as e:
        print("Error",e)
    except ZeroDivisionError as e:
        print('divide-',e)


def call_another( a, b):
    try:
       return a/b
    except:
        raise ZeroDivisionError('Error message from error occuring method')


if __name__ == '__main__':
    test()