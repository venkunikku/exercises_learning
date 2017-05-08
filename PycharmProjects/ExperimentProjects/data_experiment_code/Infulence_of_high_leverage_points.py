import pandas as pd
import matplotlib.pyplot as plt


def high_infulence_points_in_data():
    dtype_dict = {'HousePrice': int, 'HsPrc ($10,000)': float, 'CrimeRate': float, 'MilesPhila': float, 'PopChg': float,
                  'Name': str, 'County': str}

    df = pd.read_csv('../data/Philadelphia_Crime_Rate_noNA.csv',dtype=dtype_dict)
    print(df.dtypes)

    #f, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, sharex='col', sharey='row',squeeze=False,figsize=(15,15))

    fig1 = plt.figure('Plotting all the data in the dataset- fig1')
    ax1 = fig1.add_subplot(111)

    ax1.scatter(df['CrimeRate'],df['HousePrice'])
    fig1.show()

    #get slop and intercept for the data
    intercept, slope = simple_linear_regression_with_mean(df['CrimeRate'], df['HousePrice'])
    print(intercept, slope)

    predicted = []

    for i in df['CrimeRate']:
        pred = get_regression_predictions(i, intercept, slope)
        predicted.append(pred)

    print(predicted)

    fig2 = plt.figure('Actual vs Predicted (fitted line using the data)- fig2')
    ax2 = fig2.add_subplot(111)

    ax2.plot(df['CrimeRate'], df['HousePrice'],"."
            ,df['CrimeRate'],predicted,'-',color='r')


    # data with no recordds that is having more crime rate which is the outlies on the x-axis
    sales_noCC = df[df['MilesPhila'] != 0.0]

    fig3 = plt.figure('Plot by removing high leverage point- fig3')
    ax3 = fig3.add_subplot(111)
    ax3.scatter(sales_noCC['CrimeRate'],sales_noCC['HousePrice'])

    intercept, slope = simple_linear_regression_with_mean(sales_noCC['CrimeRate'], sales_noCC['HousePrice'])
    print("New Slope and Intercept after removing the high infulectial point")
    print(intercept
          , slope)

    predicted2 = []

    for i in sales_noCC['CrimeRate']:
        pred = get_regression_predictions(i, intercept, slope)
        predicted2.append(pred)

    fig4 = plt.figure('Actual vs Predicted by removing high leverage points- fig4')
    ax4 = fig4.add_subplot(111)
    ax4.plot(sales_noCC['CrimeRate'], sales_noCC['HousePrice'], "."
             , sales_noCC['CrimeRate'], predicted2, '-')


    # now remove highend houses on the Y-axis. This will not differ much of the regression coefficients
    sales_nohightend = sales_noCC[sales_noCC['HousePrice'] < 350000 ]

    intercept_nohightend, slope_nohighend = simple_linear_regression_with_mean(sales_nohightend['CrimeRate'],
                                                                               sales_nohightend['HousePrice'])

    print("New Slope and Intercept after removing the high prices house along y-axis point")
    print(intercept_nohightend
          , slope_nohighend)

    predicted3 = []

    for i in sales_noCC['CrimeRate']:
        pred = get_regression_predictions(i, intercept, slope)
        predicted3.append(pred)





    plt.show()
    #input()

def simple_linear_regression_with_mean(input_feature, output):
    x = input_feature
    y = output

    numerator = ((x * y).mean()) - (x.mean()) * (y.mean())
    denominator = ((x ** 2).mean()) - (x.mean()) * (x.mean())
    slope = numerator / denominator

    intercept = y.mean() - slope * (x.mean())
    print("Mean Numerator", numerator, 'Mean Denominator', denominator, 'n/d', slope, 'inter', intercept)
    return intercept, slope


def get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope):
    y = sqft_intercept + (sqft_slope * my_house_sqft)
    return y

if __name__ == '__main__':
    high_infulence_points_in_data()