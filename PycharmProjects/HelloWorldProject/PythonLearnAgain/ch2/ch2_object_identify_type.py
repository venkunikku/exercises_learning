
def object_reference_test():
    a = [1,2,3,4,5,6]
    b = [1,2,3,4,5,6]
    c = a

    # refering to object location in memeory using 'is'
    if a is c:
        print('refering to object in memeory')
    if type(a) is type(b):
        print('matching the type of the object- meaning testing of \'list\' type')
    if a == b:
        print('matching the values in two objects')

def better_way_to_object_reference():

    a = [1,2,3,4,5,6]
    b = [1,2,3,4,5,6]
    c = {}

    # this is better way than using type(a) == type(b)
    # this help with inheritance class to check the instance as well
    if isinstance(a,list):
        print('Checking type of the object using isinstance')
    if isinstance(c,dict):
        print('checking for dictionary type')

    # above method is better than this. Having this here for showing different options

    if type(a) is list:
        print('List-  but not recommended way')

if __name__ == '__main__':
    object_reference_test()
    better_way_to_object_reference()