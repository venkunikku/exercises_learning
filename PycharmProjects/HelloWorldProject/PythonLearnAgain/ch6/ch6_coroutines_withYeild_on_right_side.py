def co_routine():
    print("Ready to receive")
    while True:
        n = (yield )
        #print('Got following %d' % n)


def co_routine_the_accepts_text(delimiter = None):
    print('rady to plit')
    result = None
    while True:
        line = (yield result)
        result = line.split(delimiter)




if __name__ == '__main__':
    r = co_routine()
    r.__next__() # Advance to first Yeild. THIS IS NECESSARY
    r.send(100)
    r.send(200)
    r.close() # Closing the Corouties else will keep running. This also raises GeneratorExit exception like Generators
    # r.send(100) # if you try to send after close a StopIteration exceptino is thrown


    try:
        c = co_routine()
        c.__next__()  # instead of this you can create a decorator to perform next
        r.throw(RuntimeError, 'some message')  # you can throw an exception in this mannner - inside a coroutine
    except Exception as e:
        print(e)


    s = co_routine_the_accepts_text()
    s.__next__() # first time Yield returns NONE.
    print(s.send("A,B,C"))
    # s.__next__() cannot do a second time next

    p = co_routine_the_accepts_text('_')
    p.__next__()
    print(p.send('A_B_C'))

    # you cannot do this. This only works for number. You should have (yield results) for text.
    d = co_routine()
    d.__next__()
    # print('without (yield result) returns:',d.send("Test"))
