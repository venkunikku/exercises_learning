import Quandl
import pandas as pd
import pickle

pickle_file_name = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/fifty_state_quandle_data_pickle_searilize'
csv_file_path_for_quandle_data = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/quandle_data_from_pickle_code.csv'
generic_path = '/Users/venkuburagadda/PycharmProjects/Data_Analysis_Pandas/src/data/'


def getfiftystate():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    # Reading html and converting all the data to dataframe


    # print(fifty_states)
    # print(fifty_states[0])
    # print(fifty_states[0][0])
    return fifty_states[0][0][1:] # this will graph 0 item in the data farme and then outof the 0the elemet of elemnt and all elemnts


def getquandledata_and_pickle_it():
    api_key = 'yd5yEkadZUx1Mu4i4oXj'
    #qdf = Quandl.get('FMAC/HPI_AZ',authtoken=api_key)
    #print(qdf.head(50))

    fifty_states = getfiftystate() # get fifty states for building query
    all_datafram = pd.DataFrame() # creating an empty data frame
    for abb in fifty_states:
        query = 'FMAC/HPI_'+str(abb)
        print('*******gettind data for -*****:'+query)
        # li.append(abbvr) creating a list

        # getting data from Quandl
        df = Quandl.get(query,authtoken=api_key)
        df.rename(columns={'Value': str(query)}, inplace=True)
        if all_datafram.empty: # if empyt in the first run just assing df data frame to all_dataframe
            all_datafram = df;
        else :
            all_datafram = all_datafram.join(df) # if not empty basically after the first run, just join to the all_dataframe

    print('*****head after all the pulling***********')
    print(all_datafram.head())

    # you can save to a csv or you can pickle. Below is saving to CSV
    all_datafram.to_csv(csv_file_path_for_quandle_data)


    #pickel the data
    with open(pickle_file_name,'wb') as pickel_out:
        pickle.dump(all_datafram,pickel_out)


def load_data_from_pickle_searilized():
    with open(pickle_file_name,'rb') as pickle_in:
        pickle_saved_data = pickle.load(pickle_in)
    return pickle_saved_data

# pandas way to pickle
def panda_way_to_pickle_data(dataframe):
    #pandas way to pickle.
    dataframe.to_pickle(generic_path+'fifty_states_pickle_using_pandas_methods_searlize')
    #pandas way to load data from pickle.
    loading_same_data_for_testing = pd.read_pickle(generic_path+'fifty_states_pickle_using_pandas_methods_searlize')
    print('**************** loaded data from panda pickeled *******************')
    print(loading_same_data_for_testing.head())


def test():
    fifty_states = getfiftystate()  # get fifty states for building query

    for abb in fifty_states:
        query = 'FMAC/HPI_' + str(abb)
        print(abb,abb[0])

if __name__ == '__main__':
    #getquandledata_and_pickle_it()
    #pickel_save_data =  load_data_from_pickle_searilized()
    #print(pickel_save_data)

    #panda_way_to_pickle_data(pickel_save_data) # just passing the dataframe to save it using pandas pickel
    test()


