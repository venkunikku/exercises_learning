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

    figure = plt.figure()
    axis = plt.subplot2grid((1, 1), (0, 0))

    # load data from pickle
    all_state = pd.read_pickle(pickle_file_name)
    #tx = all_state['FMAC/HPI_TX'].resample('A', how='mean') # Default is mean.  A = annula, D= day look online for other details.
    tx = all_state['FMAC/HPI_TX'].resample('A').mean() # Default is mean.  A = annula, D= day look online for other details.
    print(tx.head())

    #ploting 1 year (annual) data here
    # when using subplot2grid it does not get the lables by default
    tx.plot(ax = axis,label='Yearly Data for TX')
    #ploting TX data from orginal datafrmae
    all_state['FMAC/HPI_TX'].plot(ax = axis, label='Monthly Data for TX')
    plt.legend(loc=4) #loc will be placing the legend at the bottom
    #plt.show()

    #ploting high low
    tx_ohlc = all_state['FMAC/HPI_TX'].resample('A').ohlc() # open high low close

    all_state['FMAC/HPI_TX'].plot(ax=axis, label='Monthly Data for TX')
    tx_ohlc.plot(ax=axis) # note this show not have a lable
    print(tx_ohlc)
    print('******** printing texas data ***********')
    print(all_state['FMAC/HPI_TX'])
    plt.legend(loc=4)
    plt.show()

    # Trying to convert to json
    #tx_ohlc.to_json(data_frame_to_json)


if __name__ == '__main__':
    test()