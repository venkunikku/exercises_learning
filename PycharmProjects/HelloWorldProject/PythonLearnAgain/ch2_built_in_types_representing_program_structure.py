def test(a, b=None, c=200):

    ''' this function does specfic operations '''

    print(type(str))
    print(type(set))
    print(a+b+c)

def attributes_of_user_definted_and_internal_fuction():
    print('inside')

class A():

    def get_items(self,a):
        print('Calling and printing',a)
        return a

    @classmethod
    def class_method(cls,arg):
        print('Inside calss mthod')
        print('Value: ',cls.value)
        print(arg)
    @staticmethod
    def static_method(arg):
        print(arg)

if __name__ == '__main__':
    test(100,20)
    bar = lambda x, y: x + y
    s =bar(1,2)
    print(s)

    attributes_of_user_definted_and_internal_fuction()

    # user definted and interanl fucntion have following attributes
    # these are applicable even for lambda operator
    print('doc',test.__doc__)
    print('name',test.__name__)
    print('dict',test.__dict__)
    print('code',test.__code__)
    print('defaults',test.__defaults__)
    print('globals',test.__globals__)
    print('closure',test.__closure__)

    class_obecj = A();
    m1 = class_obecj.get_items #bouding method
    print('Calling on the object',m1(10))

    static = A.get_items
    static(class_obecj,'calling by passing object of class A as first argument')

    c_method = A.class_method
    print(c_method(100))
