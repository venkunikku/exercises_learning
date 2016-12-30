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

    # add a new column and resample the data to 1 year
    all_state['TX1yr'] = all_state['FMAC/HPI_TX'].resample('A').mean()

    #all_state2 = all_state
    #all_state2[['open','high','low','close']] = all_state2['FMAC/HPI_TX'].resample('A').ohlc()
    print(all_state[['FMAC/HPI_TX','TX1yr']].head(15))


    #optoin1 is to delete or drop all the NaN

    # we will not be able to graph if dropna is not here. Try it
    #all_state.dropna(inplace=True)
    #all_state.dropna(how='all',inplace=True) # this will drop the whole row if it has all NaN  this would grpah too.


    #Option2 fill
    #all_state.fillna(method='ffill',inplace=True) # ffill -forward fill/ bfill - backward fill
    #all_state.fillna(method='bfill',inplace=True)
    #all_state.fillna(value=-99999,inplace=True)

    all_state.fillna(value=-99999,limit=10,inplace=True)
    print('How many are nulls or nan\'s')
    #ble line check if isnull and only sums non nana
    print(all_state.isnull().values.sum())

    print('********** Print after ******************')
    print(all_state[['FMAC/HPI_TX', 'TX1yr']].head(15))

    axis = plt.subplot2grid((1, 1), (0, 0))

    all_state[['FMAC/HPI_TX', 'TX1yr']].plot(ax = axis)
    plt.legend().remove()
    plt.show()


if __name__ == '__main__':
    test()