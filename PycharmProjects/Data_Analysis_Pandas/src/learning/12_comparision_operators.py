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
    bridge_height = {'meters': [10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
    #bridge_height_modified = {'meters': [10.26, 10.31, 10.27, 10.22, 10.23, 62.42, 10.28, 10.25, 10.31]
    #                          ,'Day':[1,2,3,4,5,6,7,8,9]}


    df = pd.DataFrame(bridge_height)



    df['STD'] = df['meters'].rolling(window=2).std()

    print(df)
    df_desc = df.describe()['meters']['std']
    print(df_desc)

    df = df[ (df['STD'] < df_desc) ]
    print(df)

    axis = plt.subplot2grid((1, 1), (0, 0))

    df['meters'].plot(ax= axis)
    plt.show()


if __name__ == '__main__':
    test()
