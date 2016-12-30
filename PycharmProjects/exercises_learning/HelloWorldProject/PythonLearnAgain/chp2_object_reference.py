import sys
import os


def object_reference():
    a = {}
    b = {}
    a['b']= b
     #object reference count can be found this way
    print(' Reference count of a:', sys.getrefcount(a))



if __name__ == '__main__':
    object_reference()

