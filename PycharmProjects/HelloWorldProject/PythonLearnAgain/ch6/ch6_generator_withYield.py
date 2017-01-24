def countdown(n):
    print('counting down {0}'.format(n))
    try:
        while n > 0:
            yield n
            n -= 1
    except GeneratorExit:
        print('Someone called Close method')

    return


if __name__  == '__main__':
    c = countdown(10)
    for i in c:
        print(i)
        if i == 5:
            c.close() # will close the generator
            #pass

    print('Sum:',sum(countdown(10)))
    #print(c.__next__())
