class A():

    @classmethod
    def start(cls,arg):
        cls(arg,arg+1)

    @classmethod
    def end(cls,arg1,arg2):
        print('Summing up', arg1+arg2)


if __name__ == '__main__':
    a = A()
    A.start(a,1)