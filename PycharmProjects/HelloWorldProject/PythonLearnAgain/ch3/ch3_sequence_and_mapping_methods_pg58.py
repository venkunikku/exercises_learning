class IterationTestClass():
    # if you definte contains methods you can use 'in' operator
    def __contains__(self, item):
        print('Inside the contains method')
        a = isinstance(item, list)
        return a

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, stride = item.indices(len(self))
            for i in range(start, stop, stride):
                print(i)


def slice_testing():
    data = """\
    0010GEORGE JETSON    12345 SPACESHIP ST   HOUSTON       TX
    0020WILE E COYOTE    312 ACME BLVD        TUCSON        AZ
    0030FRED FLINTSTONE  246 GRANITE LANE     BEDROCK       CA
    0040JONNY QUEST      31416 SCIENCE AVE    PALO ALTO     CA""".splitlines()
    print(data)

    tuple_slices = [(0, 4), (4, 21), (21, 42), (42, 56), (56, 58)]
    field_slices = [slice(*fielddef) for fielddef in tuple_slices]
    print(field_slices)

    fields = "id name address city state".split()
    print(fields)

    for rec in data:
        for field, slicee in zip(fields, field_slices):
            print(field, ':', rec.strip()[slicee])
        print()


if __name__ == '__main__':
    iter_object = IterationTestClass();

    li = [10, 29]
    if li in iter_object:
        print('It worked')

    # a = iter_object[0:100:10]
    slice_testing()
