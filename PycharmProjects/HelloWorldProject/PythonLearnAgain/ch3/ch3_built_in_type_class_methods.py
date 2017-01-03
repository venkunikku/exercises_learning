class A():
    def name(self):
        return "name returned"


class B():
    def no_name_method(self):
        return "no name method here"


if __name__ == '__main__':
    obA = A()
    obB = B()

    a = A.name
    print("In Python3 raw function object is store in a : ", a)
    # unbound method calls
    print(a(obA))

    # In Pyhtong 3 there is not type check on the object passed
    print(a(obB))

    print(a.__class__)
