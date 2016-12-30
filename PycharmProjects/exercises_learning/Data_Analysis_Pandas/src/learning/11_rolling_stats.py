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
data_frame_to_json = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/data_frame_to_json.json'


def test():

    # get the data from pickle
    all_state = pd.read_pickle(pickle_file_name)
    #all_state['TX12MA']  = pd.rolling_mean(all_state['FMAC/HPI_TX'],12)
    #all_state['TX12STD'] = pd.rolling_std(all_state['FMAC/HPI_TX'],12)

    all_state['TX12MA'] = all_state['FMAC/HPI_TX'].rolling(center=False,window=12).mean()
    all_state['TX12STD'] = all_state['FMAC/HPI_TX'].rolling(center=False, window=12).std()


    print(all_state[['TX12MA','FMAC/HPI_TX']])
    print(all_state[['TX12MA', 'FMAC/HPI_TX','TX12STD']])

    #plotting
    figure = plt.figure()
    axis1 = plt.subplot2grid((2, 1), (0, 0))
    axis2 = plt.subplot2grid((2, 1), (1, 0), sharex=axis1)
    #axis3 = plt.subplot2grid((3, 1), (2, 0), sharex=axis1)

    #all_state[['TX12MA', 'FMAC/HPI_TX']].plot(ax=axis1)
    #all_state['TX12STD'].plot(ax=axis2)



    # we can get rolling correlation betwen two
    # TX_AK_12corr = pd.rolling_corr(all_state['FMAC/HPI_TX'],all_state['FMAC/HPI_AK'],12)
    TX_AK_12corr = all_state['FMAC/HPI_TX'].rolling(window=12).corr(other=all_state['FMAC/HPI_AK'])

    all_state[['FMAC/HPI_TX','FMAC/HPI_AK']].plot(ax=axis1)
    TX_AK_12corr.plot(ax=axis2,label='TX_AK_Corr')
    #all_state.plot(ax=axis3)

    plt.legend(loc=4)
    plt.show()

if __name__ == '__main__':
    test()
