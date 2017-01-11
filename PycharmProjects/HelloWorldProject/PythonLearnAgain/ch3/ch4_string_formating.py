def test():
    ''' conversion speecifier starts with % and ends with one of value from the String formatting Conversion table'''

    a = 46
    r = 'a has %s '  % a
    with_width =  'a has %20s  space before 46 by sing  per  20s'  % a
    with_width_right = 'a has %-20s  space after 46 by using per -20s' % a
    print(r)
    print(with_width)
    print('widht on right',with_width_right)

    item = {'lastname': 'john', 'name': 'john'}

    s = 'this is an apple'
    print('%.2s'  % s ,'::::Prints only first 2 chars')

    b = 13.142783
    print('%.*f' % (3,b) , ':::It has to be a tubple when you use aserisk *. This will format the float number to 3 deci')

    print('%d is coming from a . %s is coming from dictionary' % (a,item['lastname']))

    print('%(name)s is coming from dictionary' % item)

    stock = {
        'name': 'GOOG',
        'shares': 100,
        'price': 490.10}

    print('"%(shares)d of %(name)s at %(price)0.2f' % stock)

    # you can use vars to get the vars from the programs
    print('%(a)d as number -  %(s)s as String - %(item)s' % vars())

if __name__ == '__main__':
    test()
