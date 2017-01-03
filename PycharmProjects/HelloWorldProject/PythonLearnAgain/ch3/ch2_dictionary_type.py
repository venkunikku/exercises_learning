def test():
    s = 1/3;
    print(s)
    print(len(str(s)))


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

        # notice - how append is done on the list object of the dictionary. This is efficient way.
        # DO NOT DO item['array'] = item['array']+[10]. This will creat a new copy of the item['array']. if any other
        # var is making a shallo copy that will not be updated if you do it without append.
        item['array'].append(10)

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

        print('************ defaultdict ******************')
        # we have defaultdict method in collections in order to initialize a dictionary with a a default type
        # defaultdict inheritance from dict. So all method still valid execpt one method that is ovveridden
        from collections import defaultdict
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('orange', '')]
        d = defaultdict(list)

        for k, v in s:
            d[k].append(v)

        print('printing defaultdict values ', d)
        print('************ defaultdict- end ******************')

        print('************* usind defaultdict to count ***************')
        s = 'mississippi in a ssaammpple'
        d = defaultdict(int)
        for k in s:
            d[k] += 1
        print('Printing counting letters in a word', d)

        # Above we use init to initialize a word when the first item there is not value to 0. And then increment it.
        # we can use below way to initialize to something default. Using itertools.repeat()
        print('************* usind defaultdict to count - end ***************')

        print('*************** defaultdict using our own default value************')

        d = defaultdict(constant_factory('<missing nothing provided>'))
        d.update(name='john', age=10)
        print(d)
        print('This provides some default values automatically', d['lastname'])
        print('*************** defaultdict using our own default value - end ************')

def constant_factory(value):
    # import itertools
    return lambda: value

if __name__ == '__main__':
    test()
    dictionary_test()