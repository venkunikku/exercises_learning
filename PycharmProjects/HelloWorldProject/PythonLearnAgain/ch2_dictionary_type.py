
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

        #mapping key to the values
        # it will not effect item dic. It will create a new dict
        s = [1,2,3,4,5,'hello']
        print(item.fromkeys(s,'same value for all'))

        # or you can use dict.formkeys()
        print(dict.fromkeys(s,'same values for all'))

        print(item.items())
        print(type(item.keys()))

        print(list(item.items()))

if __name__ == '__main__':
    test()
    dictionary_test()