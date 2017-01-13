class Iterator:
    # def __new__(cls, *args, **kwargs):
    #    print("Called when new object is created")

    # def __init__(self, a):
    #    print("Called when object is created")

    # def __del__(self):
    #    print("called when object is destored")
    li = []

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self  # this shouls return an iterator. If the same class is implementing __next__ the it can return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


if __name__ == '__main__':
    a = Iterator(10)

    for i in a:
        print(i)
