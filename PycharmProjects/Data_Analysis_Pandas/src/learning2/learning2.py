import pandas as pd
import matplotlib.pyplot as plt
from numpy import random


def data_generate_seed():
    name = ['Bob', 'Mat', 'Bill', 'John', 'Apple']
    random_name = [name[random.randint(0, len(name))] for i in range(1000)]
    births = [random.randint(0, 1000) for i in range(1000)]
    babay_data_set = list(zip(random_name, births))
    df = pd.DataFrame(data=babay_data_set, columns=['Name', 'Births'])

    df.to_csv('babayname.csv', index=False, header=False)
    # random.seed(500)

    # reading from csv
    df_csv = pd.read_csv('babayname.csv',names=['Name','Births'])

    print('Getting details about the data set')
    print(df_csv.info())

    sorted_data_set = df_csv.sort_values(by='Name',ascending=False)
    print(sorted_data_set.head())
    print(sorted_data_set.tail())

    print(df_csv['Name'].unique())

    # Method#1
    ''' if you want to print the unique values '''
    print('Priting all the unique values below: ')
    for x in df_csv['Name'].unique():
        print(x)

    # Method#2
    print('Describing the column name below:')
    print(df_csv['Name'].describe())

    ''' Grouping the data '''
    name = df_csv.groupby(by='Name')
    ''' Apply sum function to group by object'''
    df_with_sum = name.sum()
    print(df_with_sum)

    df_with_sum['Births'].plot.bar()
    plt.show()


if __name__ == '__main__':
    data_generate_seed()
