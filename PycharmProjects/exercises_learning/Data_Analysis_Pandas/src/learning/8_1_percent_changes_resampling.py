import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import Quandl
import pickle
style.use('fivethirtyeight')
#style.use('pyplot')

pickle_file_average_rate_index_all_states = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/fifty_state_quandle_data_avg_rate_change.pickle'
csv_file_path_for_quandle_data = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/quandle_data_from_pickle_code.csv'
generic_path = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/'
api_key = 'yd5yEkadZUx1Mu4i4oXj'
HPI_benchmark_data_file_path = generic_path+'HPI_USA.pickle'

def test():
    loading_same_data_for_testing = pd.read_pickle(generic_path + 'fifty_states_pickle_using_pandas_methods_searlize')
    print(loading_same_data_for_testing)

    # createing a new colum
    ##loading_same_data_for_testing['FMAC/HPI_AL_NEW'] = loading_same_data_for_testing['FMAC/HPI_AL']*100
    ##print(loading_same_data_for_testing[['FMAC/HPI_AL_NEW','FMAC/HPI_AL']].mean())
    ##print(loading_same_data_for_testing['FMAC/HPI_AL_NEW'].mean())
    ##print(loading_same_data_for_testing['FMAC/HPI_AL_NEW'])


    loading_same_data_for_testing.plot()
    plt.legend().remove()
    plt.show()


def percent_change_pandas():
    loading_same_data_for_testing = pd.read_pickle(generic_path + 'fifty_states_pickle_using_pandas_methods_searlize')
    loading_same_data_for_testing = loading_same_data_for_testing.pct_change();
    loading_same_data_for_testing.plot()
    print('******* PCT Change using Pandas function of pct_change() ************')
    print(loading_same_data_for_testing.head())
    plt.legend().remove()
    plt.show()


def getfiftystate():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    # Reading html and converting all the data to dataframe


    # print(fifty_states)
    # print(fifty_states[0])
    # print(fifty_states[0][0])
    return fifty_states[0][0][1:] # this will graph 0 item in the data farme and then outof the 0the elemet of elemnt and all elemnts


def getquandledata_and_pickle_it():

    #qdf = Quandl.get('FMAC/HPI_AZ',authtoken=api_key)
    #print(qdf.head(50))

    fifty_states = getfiftystate() # get fifty states for building query
    all_datafram = pd.DataFrame() # creating an empty data frame
    for abb in fifty_states:
        query = 'FMAC/HPI_'+str(abb)
        print('*******gettind data for -*****:'+query)


        # getting data from Quandl
        df = Quandl.get(query,authtoken=api_key)
        # all columsn comes as value for every state so we are renaming.
        df.rename(columns={'Value': str(query)}, inplace=True)

        #before joining we are calcuating the rate of changes for each of the datafram that quandle retruns
        '''
            (current value - first value / first valye) * 100 to calculate rate of change
        '''
        print('df[query]',df[query])
        print('df[query][0]',df[query][0])
        df[query] =  ( df[query] - df[query][0] / df[query][0] )  * 100
        print('After calculation',df[query])
        df.to_html(generic_path + 'html_format_avg_rate_change'+str(abb)+'.html')
        if all_datafram.empty: # if empyt in the first run just assing df data frame to all_dataframe
            all_datafram = df;
        else :
            all_datafram = all_datafram.join(df) # if not empty basically after the first run, just join to the all_dataframe

    print('*****head after all the pulling***********')
    print(all_datafram.head())

    #pickel the data
    with open(pickle_file_average_rate_index_all_states, 'wb') as pickel_out:
        pickle.dump(all_datafram,pickel_out)


def percent_change_by_calcuating_before_join_from_quandle():
    loading_same_data_for_testing = pd.read_pickle(pickle_file_average_rate_index_all_states)
    loading_same_data_for_testing.plot()
    plt.legend().remove()
    plt.show()

def HPI_Benchmark():
    df = Quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df['Value'] = ( ( df['Value'] - df['Value'][0] ) / df['Value'][0] ) * 100
    print(df.head(100))
    df.to_pickle(HPI_benchmark_data_file_path)
    return df


def plot_USA_HPI_benchmark_data():
    df = pd.read_pickle(HPI_benchmark_data_file_path)
    df.plot()
    plt.legend().remove()
    plt.show()


def combine_HPI_of_all_state_with_HIP_USA():
    #graph config
    figure = plt.figure()
    axis1 = plt.subplot2grid((1, 1), (0, 0)) # grid is 1,1 and start the line from (0,0)

    # getting two data sets for ploting
    all_states = pd.read_pickle(pickle_file_average_rate_index_all_states)
    all_usa = pd.read_pickle(HPI_benchmark_data_file_path)

    #plotting the data
    all_states.plot(ax=axis1)
    all_usa.plot(ax=axis1,color='k',linewidth=10) # color-'k' is black and linewidht is the how big the line is

    plt.legend().remove()
    plt.show()



if __name__ == '__main__':
    #test()

    #getquandledata_and_pickle_it()
    #percent_change_pandas()

    #percent_change_by_calcuating_before_join_from_quandle()

    # all above methods are state wide. Below is US wide
    #all_USA_HPI_benchmark_data = HPI_Benchmark()
    #plot_USA_HPI_benchmark_data()

    combine_HPI_of_all_state_with_HIP_USA()
