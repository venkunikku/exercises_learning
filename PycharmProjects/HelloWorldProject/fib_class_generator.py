#Example of definig a class

class Fib():
    """ first statemet of the calss."""
    def __init__(self,a=0,b=1):
        print('calling the contructor')
        self.a = a
        self.b = b

    def fib_generator(self):
        while True:
            yield(self.b)
            self.a,self.b = self.b,self.a+self.b


#def call():
print('into the calling function')
f=Fib(0,1)
for x in f.fib_generator():
    if x>100: break
    print(x)


