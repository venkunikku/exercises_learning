import Quandl
import pandas as pd

def test():
    api_key = 'yd5yEkadZUx1Mu4i4oXj'
    qdf = Quandl.get('FMAC/HPI_AZ',authtoken=api_key)
    print(qdf.head(50))


    # Reading html and converting all the data to dataframe

    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    #print(fifty_states)
    #print(fifty_states[0])
    #print(fifty_states[0][0])
    li = []
    for abb in fifty_states[0][0][1:]:
        abbvr = 'FMAC/HPI_'+str(abb)
        print(abbvr)
        li.append(abbvr)

    print(li)

if __name__ == '__main__':
    test()

