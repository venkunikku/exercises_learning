

try:
    f = open("somefile.txt")
    for ff in f.readline():
        print(ff)
except IOError as e:
        print(e)

def method():
        print('more than 4 spaces')
        print('jk')

if __name__=='__main__': method()
