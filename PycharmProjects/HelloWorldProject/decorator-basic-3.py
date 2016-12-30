def p_decorator(func):
    def wrapped_function(name):
        return "<p> {0} </p>".format(func(name))
    return wrapped_function # it returns a wrapped call with following "<p> get_text(name) </p>


def div_decorator(func):
    def wrapped_function(name):
        return '<div> {0} </div>'.format(func(name))
    return wrapped_function  # '<div> def wrapped_function_div(function_name): p_decorator(function_name) </div>'


@div_decorator
@p_decorator
def get_text(name):
    return "Hello" + name


def test():
    temp = get_text("John")
    print(temp)


if __name__ == '__main__':
    test()