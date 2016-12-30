import pandas as pd

def test():

    df1 = pd.DataFrame({'HPI' :[80 ,85 ,88 ,85],
                        'Int_rate' :[2, 3, 2, 2],
                        'US_GDP_Thousands' :[50, 55, 65, 55]},
                       index = [2001, 2002, 2003, 2004])

    df1_same = pd.DataFrame({'HPI': [80, 85, 88, 85],
                        'Int_rate': [2, 3, 2, 2],
                        'US_GDP_Thousands': [50, 55, 65, 55]},
                       index=[2001, 2002, 2003, 2004])

    df2 = pd.DataFrame({'HPI' :[80 ,85 ,88 ,85],
                        'Int_rate' :[2, 3, 2, 2],
                        'US_GDP_Thousands' :[50, 55, 65, 55]},
                       index = [2001, 2006, 2007, 2008])

    df3 = pd.DataFrame({'HPI' :[80 ,85 ,88 ,85],
                        'Int_rate' :[2, 3, 2, 2],
                        'Low_tier_HPI' :[50, 52, 50, 53]},
                       index = [2001, 2002, 2003, 2004])

    # all these are same.
    print('*****df1 and df2 and df3 Concat*******')
    concat = pd.concat([df1,df2,df3])
    print(concat)

    print('*****df1 and df2 CONCAT*******')
    concat = pd.concat([df1,df2])
    print(concat)

    print('*****df1 and df3 append*******')
    concat = pd.concat([df1, df3])
    print(concat)

    print('*****df1 and df2 append*******')
    apnd = df1.append(df2)
    print(apnd)

    print('***** df3.append(df2.append(df1)) append*******')
    apnd = df3.append(df2.append(df1))
    print(apnd)

    print('***** df1.append(df2.append(df3)) append*******')
    apnd = df1.append(df2.append(df3))
    print(apnd)

    print('***** Creating a series and then appending to df1 ** Can only append when ingnore_index=True on Series *****')
    ser = pd.Series([10,20,30], index=['HPI','Int_rate','US_GDP_Thousands'])
    df4 = df1.append(ser,ignore_index=True)
    print(df4)


    # create a series
if __name__ == '__main__':
    test()
