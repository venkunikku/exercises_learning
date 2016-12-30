#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

def test():
    df = pd.read_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/FMAC-HPI_AZ.csv')
    df.set_index('Date',inplace=True)
    #print(df.head())

    #save data to a csv
    df.to_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/csv_created_by_pandas.csv')

    # you can specify the index column during the reading of the file itself.
    df2 = pd.read_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/csv_created_by_pandas.csv',
                      index_col=0)
    print(df.head())

    # you can rename a column
    df.columns = ['Arizona_Home_Price_Index']
    print('Instead of Value now we have a name for the column. This help if we import multiple files')
    print(df.head())

    print('now if you save this file then it will save the column we used above')
    df.to_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/csv_created_by_pandas_w_col_name.csv')

    # if you dont need any columns in the file you save then you set this header=false.
    df.to_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/csv_created_by_pandas_w_no_col_name.csv',
              header=False)

    #importing a file without any head. you can provide columns name

    df = pd.read_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/csv_created_by_pandas_w_no_col_name.csv',
                     names=['Date', 'Austin_HPI_ReNamed'],index_col=0)

    print(df.head())

    #Convert this data into a html file
    df.to_html('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/data.html')

    #renaming columsn
    #df = pd.read_csv('/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/csv_created_by_pandas_w_col_name.csv')
    #print(df.head())
    df.rename(columns={'Austin_HPI_ReNamed':'7706_HPI'},inplace=True)
    print('Renaming columns')
    print(df.head())

if __name__ == '__main__':
    test()

