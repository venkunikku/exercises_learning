def test_set():
    s1 = set([1, 2, 3, 4, 5,7])
    s2 = set([1, 2, 3, 4, 5, 6])
    print(s1)
    print(s2)

    #difference
    print(s1.difference(s2))
    print(s2.difference(s1))

    #intersections
    print('Intersection:',s1.intersection(s2))

    s3_copy_s1 = s1.copy()
    print('Copy of s1',s3_copy_s1)
    # Checking to if this copy is shall or deep copy
    s3_copy_s1.add(100)
    print('Update s3_copy_s1',s3_copy_s1)
    print('Checkif s1 got updated: ', s1, ' Looks like it is not. So a deep copy is created')

    s4_copy_s1 = s1;
    print('Pointing s1 object address to s4_copy_s1 object as well')
    s4_copy_s1.add(200)
    print('Checking s1 after the update to s4:',s1 , 'checking s4_copy_s1 as well: ', s4_copy_s1)

    froz_set = frozenset([1,2,3,4,5,6])
    print(froz_set)


    # any pythong object that supports iteration can be used in the set operations
    li = [10,11,12,13]
    print(s1.difference(li))

    item = {
        1:11,
        2:21
    }
    print('You do set operations on dict iteration type as well',s1.difference(item))

    string = '123457'
    print(s1.difference(string))

    print(s1.intersection_update(item))
    # match between s1 and item and then only have the matches in both.
    print('Keys are matched to the set in s1:', s1)

# there methods that just returns True/False or new set. And there are methods that modify the orginal object itself.


if __name__ == '__main__':
    test_set()