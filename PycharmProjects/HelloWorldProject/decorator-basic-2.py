
def p_decorator(func):
    def wrapped_function(name):
        return "<p> {0} </p>".format(func(name))
    return wrapped_function # it returns a wrapped call with following "<p> get_text(name) </p>


def div_decorator(func):
    def wrapped_function(name):
        return '<div> {0} </div>'.format(func(name))
    return wrapped_function  # '<div> def wrapped_function_div(function_name): p_decorator(function_name) </div>'


def get_text(name):
    return "Hello" + name


def test():
    var1 = p_decorator(get_text)
    print(var1('john'))

    var2 = div_decorator(p_decorator(get_text))
    # '<div> def wrapped_function(name): p_decorator(name) </div>'
    #  wrapped_function(get_text): p_decorator(get_text)-> this method returns another methods
    # p_decorator(get_text) returns following
    # <div> wrapped_function(name)  </div>

    print('var2',type(var2))
    print('Var2',var2('Joohn'))
    # var3 = var2(get_text)
    # <div> wrapped_function(name)  </div>
    # <div> <div> <p> get_text(name)  </p> </div>


    #print('var3',type(var3))
    # <div> <div> <p> get_text("John")  </p> </div>



if __name__ == '__main__':
    test()
