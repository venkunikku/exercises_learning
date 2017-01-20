'''
2 types
1. Returning a fucntion from a fucntion. But the retured fuction is somewhere else or a different fun no part of the current
2. When the returing function is a innner function of the function we called. This hlep to develop a concept called
lazy initialization



'''

@track
def square(x):
    return x*x

def track(func):
    def callf(func):
        print('calling')
        r = func(*args,**kwargs)
        return r
    return callf


if __name__ == '__main__':
    a = square(10)