def simple_formating():
    ''' conversion speecifier starts with % and ends with one of value from the String formatting Conversion table'''

    a = 46
    b = -46
    r = 'a has %s '  % a
    with_width =  'a has %20s  space before 46 by sing  per  20s'  % a
    with_width_right = 'a has %-20s  space after 46 by using per -20s' % a
    print(r)
    print(with_width)
    print('widht on right',with_width_right)
    print('print symbol +/- even if the value is positive %+d' % a)
    print('print symbol +/- even if the value is positive %+d' % b)
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

def advanced_formating():
    '''[ [fill[align]] [sign] [0] [width] [.precision] [type]  '''


    '''fill  - eg =
    align - < > ^
    sign - + or - or ' ' (+ leading sing should be used for all #. - is default showing only for - negative. ' ' adds a space for + number
    [0] -
    widht - 10 or 20 etc
    type - is optionsl when not sepcified depending on s, d, f (string, digit, float)
    '''
    r = "{0} {1} {2}".format('GOOG', 100, 490.10)
    print(r)
    r = "{name} {shares} {price}".format(name='GOOG', shares=100, price=490.10)
    print(r)
    r = "Hello {0}, your age is {age}".format("Elwood", age=47)
    print(r)
    r = "Use {{ and }} to output single curly braces".format()
    print(r)

    stock = {'name': 'GOOG',
             'shares': 100,
             'price': 490.10}
    item = {'lastname': 'john', 'name': 'john'}

    print('Refering by object Index','{0[name]:s} is named after {1[lastname]}'.format(stock,item))
    print('Refering by object Index', '{0[name]:s} price is {0[shares]:8d}'.format(stock),'- Sepecifying the width')
    x = 3 + 4j
    print('You can use attribute reference using the object {0.real} {0.imag}'.format(x))

    name = "Elwood"
    number = 100
    neg_number = -23
    float_number = 12.4263423
    neg_float_number = -323.234
    print('{0:<10}'.format(name),'word') # < on the right side
    print('{0:>10}'.format(name),'word') # > on the left side
    print('{0:^10}'.format(name),'word') # ^ center align with 10 as the width
    print('{0:=^10}'.format(name),'word') # ^ center align with 10 as the width and fill with =

    print('{0:+d}'.format(number),'+ sing is used for + positive and - for negative. Displays for all the number') # leading sing should be use for all number
    print('{0:+d}'.format(neg_number), 'word')  # leading sing should be used for all number
    print('{0:-d}'.format(neg_number), 'minus Displays sing only for - negative # and no sign for + #')  # leading sing should be used for all number
    print('{0:-d}'.format(number), 'minus Displays sing only for - negative # and no sign for + #')  # leading sing should be used for all number
    print('{0:' 'd}'.format(number), 'minus Displays sing only for - negative # and no sign for + #')  # leading sing should be used for all number

    print('{0:.2F}'.format(float_number), '.2 precession. Looks like it is rouding to last 2 digit')  # leading sing should be used for all number

    print('{0:025d}'.format(number), 'padding the left side of the digit with 0 s. Used for binary')  # leading sing should be used for all number

    x = 42
    c = 'a'
    print('{0:10x}'.format(x),'hexa decimal with padding of 10 width')
    print('{0:b}'.format(x),'bytes for number 42')
    print('{0:x}'.format(ord(c)),'Hexa Equavalent of a for UTF-8 code point')
    print('{0:b}'.format(ord(u'\u2020')),'hexa')
    print(ord(c))

    uni = u'\u0061'
    print(ord(uni))
    print('{0:b}'.format(ord(uni)), 'unicode bytes')


    v = 97
    print('{0:b}'.format(v), 'bytes for number 97')

    y = 3.1415926
    print('{0:20.2f}'.format(y),'Haivng 20 width inforant of the number')
    print('{0:20.2%}'.format(y),'Haivng 20 width infront and % at the end of the number')

if __name__ == '__main__':
    simple_formating()
    advanced_formating()
    print(advanced_formating.__code__)
