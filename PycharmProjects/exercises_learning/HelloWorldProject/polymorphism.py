

class Quack():
    def common1(self):
        print('comment method')
class Dog():
    def common1(self):
        print('comment method in Dog')
    def common2(self):
        print('common method in 2 in Dog')

def test():
    q = Quack()
    d = Dog()
    call_a_method(q)
    call_a_method(d)
    call_a_method2(q)
    call_a_method2(d)

def call_a_method(obj):
    obj.common1();
    try:
        obj.common2()
    except AttributeError as e:
        print('No method of type Commone2 for obejct',e)

def call_a_method2(obj):
    if hasattr(obj,'common2'):
        print('it has commone2 method')
    else:
        print('it does not have common mehtod2')


if __name__ == '__main__':
    test()