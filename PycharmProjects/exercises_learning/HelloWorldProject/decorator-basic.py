

def say_hello(name):
    return "Hello"+name;


def p_decorator(func):
    def p_tag_function(name):
        return "<p>{0}</p>".format(func(name))

    return p_tag_function


def test():
    var1 = p_decorator(say_hello)
    print(type(var1))
    print(var1("John"))

    print(p_decorator(say_hello)('JohnName'))

    print(p_decorator(say_hello('JohnName')))
if __name__ == '__main__':
    test()