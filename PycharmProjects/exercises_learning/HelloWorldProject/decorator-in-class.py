from functools import wraps

class DecoreTesting(object):
    def __init__(self, before, after):
        self.before = before
        self.after =  after

    def __call__(self,func):
        @wraps(func)
        def wrapped_func_call(name):
            try:
                self.before()
                r= func(name)
            finally :
                self.after()
            return r
        return wrapped_func_call

def before():
    print("Work before")

def after():
    print('work after')

@DecoreTesting(before,after)
def my_function_call(name):
    return "Finall Gog it "+name

def test():
    s =  my_function_call('John')
    print(s)

    print('*****************')
    v = DecoreTesting(before,after)(my_function_call)("john")
    print('Type of v',type(v))
    print(v) # not sure why it is calling 2 time of before and after when i do it this way.

if __name__ == '__main__':
    test()
