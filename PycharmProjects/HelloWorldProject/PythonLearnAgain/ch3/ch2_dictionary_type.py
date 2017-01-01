
def test():
    s = 1/3;
    print(s)
    print(len(str(s)))


if __name__ == '__main__':
    def dictionary_test():
        item = {
            'no': 1,
            'desc':'description',
            'array': [1,2,3,4,5]

        }

        print(item)
        print('keys',item.keys())

        print('************Shall Copy******************')
        #Making a Shall copy of the dictionary
        shallow_copy_of_dict = item.copy()
        print('Shall Copy of the dictionary', shallow_copy_of_dict)

        item['newitem'] = 'newvalue into newitem'

        item['array'] = item['array']+[10]
        print('Oringinal Dic:', item)
        print('Shallow copy of the main dict: NO CHANGE SINCE WE DID NOT Modify object', shallow_copy_of_dict)


        print('************Shall Copy- End******************')

        #mapping key to the values
        # it will not effect item dic. It will create a new dict
        s = [1,2,3,4,5,'hello']
        print(item.fromkeys(s,'same value for all')) #doing this way gives you a 'item' type to new dict that is created
        #  from formkeys. This is the main difference between this and the below dict.fromkeys()

        # or you can use dict.formkeys()
        print(dict.fromkeys(s,'same values for all')) # this is a classMethod where you can create a new dict.

        print(item.items())
        print(type(item.keys()))

        print(list(item.items()))

if __name__ == '__main__':
    test()
    dictionary_test()