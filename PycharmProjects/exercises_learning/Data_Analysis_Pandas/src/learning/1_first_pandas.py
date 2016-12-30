#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style
import numpy as np

def test():
    # style.use('ggplot')
    print( mpl._get_cachedir() )
    web_stats = { 'Day':[1,2,3,4,5,6],
                'Visitors':[43,56,78,34,23,12],
                'Bounce_Rate':[10,20,55,64,34,23],'People':['john','x','v','b','n','m',] }
    dataframe = pd.DataFrame(web_stats) # creating data frame using dictionary
    print('Data Frame from Pandas')
    print(dataframe)
    print('Data frame Head')
    print(dataframe.head())
    print('Data frame Trail')
    print(dataframe.tail())
    print('Data frma tail last 2')
    print(dataframe.tail(2))

    # setting index to the data

    dataframe.set_index('Day',inplace=True)
    print('datafrom head')
    print(dataframe.head())

    # referencing a column
    print('peple access like dictionary')
    print(dataframe['People'])
    print('people access like attribute')
    print(dataframe.People)
    print('visitionr access like dictionray')
    print(dataframe['Visitors'])

    print('tow column data')
    #multiple columns
    print(dataframe[['Visitors','Bounce_Rate']])

    # converting to a list
    print('convert a single column to arry')
    print(dataframe['Visitors'].tolist())

    # you cannot convert multiple colums into array for that you have to use numpy
    print('Converting two columsn to an arry using numpy')
    print(np.array(dataframe[['Visitors','Bounce_Rate']]))

    # converting above numpy array of arry to dataframe

    df3 = pd.DataFrame(np.array(dataframe[['Visitors','Bounce_Rate']]))
    print('Converting NUMPY array of two columns to back to Dataframe using Pandas')
    print(df3)

if __name__ == '__main__':
    test()

