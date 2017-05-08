import pandas as pd
import matplotlib.pyplot as plt


def high_infulence_points_in_data():
    dtype_dict = {'HousePrice': int, 'HsPrc ($10,000)': float, 'CrimeRate': float, 'MilesPhila': float, 'PopChg': float,
                  'Name': str, 'County': str}

    df = pd.read_csv('../data/experiment_data/Philadelphia_Crime_Rate_noNA.csv',dtype=dtype_dict)
    print(df.dtypes)
    plt.scatter(df['CrimeRate'],df['HousePrice'])
    plt.show()

if __name__ == '__main__':
    high_infulence_points_in_data()