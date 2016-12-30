import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import Quandl
import pickle
style.use('fivethirtyeight')


pickle_file_average_rate_index_all_states = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/fifty_state_quandle_data_avg_rate_change.pickle'
csv_file_path_for_quandle_data = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/quandle_data_from_pickle_code.csv'
generic_path = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/'
api_key = 'yd5yEkadZUx1Mu4i4oXj'
HPI_benchmark_data_file_path = generic_path+'HPI_USA.pickle'
pickle_file_name = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/fifty_state_quandle_data_pickle_searilize'



def test():

    # get data from pickel
    all_state = pd.read_pickle(pickle_file_name)
    all_usa = pd.read_pickle(HPI_benchmark_data_file_path)

    # generating a corelation table for all the columns

    HPI_corelation = all_state.corr() # this will generate a martic of each state to all states
    print(HPI_corelation)

    print(HPI_corelation.describe())



if __name__ == '__main__':
    test()