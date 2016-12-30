class Egg():
    def __init__(self,kind = 'fried'):
        self.kind = kind

    def what_kind(self):
        return self.kind

def test():
    fried = Egg()
    print('Using default value in the constructor:', fried.what_kind())
    scrambled = Egg('scrambled')
    print('sending a value to the constructor as scrambled',scrambled.what_kind())

if __name__ == '__main__': test()
