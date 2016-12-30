import pandas as pd


def test():

    df1 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                        'Int_rate': [2, 3, 2, 2],
                        'US_GDP_Thousands': [50, 55, 65, 55]} )

    df3 = pd.DataFrame({'Year': [2001, 2003, 2004, 2005],
                    'Unemployment': [10, 8, 9, 20],
                    'Low_tier_HPI': [50, 52, 50, 53]} )

    print('**************** merged on left ****************')
    merge = pd.merge(df1, df3, on='Year', how='left')
    print(merge)
    merge.set_index('Year', inplace=True)
    print(merge)

    print('**************** merged on right ****************')
    right = pd.merge(df1, df3, on='Year', how='right')
    print(right)
    right.set_index('Year', inplace=True)
    print(right)

    print('**************** merged on outer- union of all keys ****************')
    outer = pd.merge(df1, df3, on='Year', how='outer')
    print(outer)
    outer.set_index('Year', inplace=True)
    print(outer)


    print('**************** merged on inner- this is th default. Basically like join ****************')
    inner = pd.merge(df1, df3, on='Year', how='inner')
    print(inner)
    inner.set_index('Year', inplace=True)
    print(inner)


    print('**************** join ****************')


    print('**************** joining df2 on df3 only df2 indexed columns are used ****************')
    # suffix is required to be set for Join
    df1.set_index('Year', inplace=True)
    df3.set_index('Year', inplace=True)
    joined = df1.join(df3)
    print(joined)

    print('**************** joinig df3 on df2- only df2 index columsn are used ****************')
    joined = df3.join(df1)
    print(joined)

    print('**************** joinig df3 on df2- only df2 using how ****************')
    joined = df3.join(df1)
    print(joined)


    print('**************** joinig df3 on df2- only df2 using how and on ****************')
    # not allowing to set on='Year' here
    joined = df3.join(df1,how='inner') # same as merge outer,inner,left,right
    print(joined)

if __name__ == '__main__':
    test()