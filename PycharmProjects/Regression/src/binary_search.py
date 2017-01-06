import sys
def binary_search2(r, guess):
    min_no = 0
    if isinstance(r,list):
        max_no = len(r) -1
    else :
        raise AttributeError
    print('min:max:',min_no,max_no)
    i = 0
    while max_no > min_no:
        print('Reference count of Min:',sys.getrefcount(min_no))
        print('Reference count of Max:', sys.getrefcount(max_no))
        avg_index = int((min_no+max_no)/2)
        print('Average Index Rounded Down to :',avg_index, 'from: ',(min_no+max_no)/2,'****',min_no,max_no)
        value_at_the_index = r[avg_index]
        print('Value at the index:', value_at_the_index)
        i += 1
        if value_at_the_index == guess :
            return (avg_index,i)
        elif value_at_the_index > guess :
            max_no = avg_index
            print('Value at the index ',avg_index,'is',value_at_the_index,'>', guess ,'so min/max is:', min_no,max_no)
        else :
            min_no = avg_index + 1
            print('Value at the index ', avg_index, 'is', value_at_the_index, '<', guess,'so min/max is:', min_no, max_no)
    else:
        return (None,None)


if __name__ == '__main__':
    data = list(range(0, 10000000, 100))
    output_tuple =  binary_search2(data, 200)
    print('It took {1} attempts to find the number. The index of the array is {0} '.format(*output_tuple))
    r = list(range(0,10))
    print(r)
    print(r[9:10])
