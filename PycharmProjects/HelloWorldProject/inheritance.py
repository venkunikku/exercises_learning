
class Animal():
    def __init__(self):
        print('Parent class constructor')

    def talk(self):
        print('talking from Animal base calss')

class Duck(Animal):
    def __init__(self):
        super().__init__()
        print('child class constructor')

    def talk(self):
        super().talk()

        print('I am talking')


class hippo():
    pass

def test():

    d = Duck();
    d.talk()

    isinstance_check_function = is_instance_check(d)
    print('checing isinstance',isinstance_check_function)

    hip = hippo()
    print(is_instance_check(hip))

def is_instance_check(obj):
    return True if isinstance(obj,Animal) else False

if __name__ == '__main__':
    test()