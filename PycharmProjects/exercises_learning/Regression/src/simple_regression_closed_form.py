import csv
import pandas as pd
import numpy as np

def pand():
    dtype_dict = {'bathrooms': float, 'waterfront': int, 'sqft_above': int, 'sqft_living15': float, 'grade': int,
                  'yr_renovated': int, 'price': float, 'bedrooms': float, 'zipcode': str, 'long': float,
                  'sqft_lot15': float, 'sqft_living': float, 'floors': str, 'condition': int, 'lat': float, 'date': str,
                  'sqft_basement': int, 'yr_built': int, 'id': str, 'sqft_lot': int, 'view': int}


    # Loading data and converting to pickle
    ##df = pd.read_csv('/Users/venkuburagadda/iPython_Notebook_Data/Regression_Actual_Course/Week1/Quize_2/kc_house_train_data.csv')
    ##df.to_pickle('/Users/venkuburagadda/PycharmProjects/Regression/src/data/housing_data_seed80.pickle')

    ##df_test = pd.read_csv('/Users/venkuburagadda/iPython_Notebook_Data/Regression_Actual_Course/Week1/Quize_2/kc_house_test_data.csv')
    ##df_test.to_pickle('/Users/venkuburagadda/PycharmProjects/Regression/src/data/housing_data_seed20.pickle')

    #Loading train data from pickle.
    loading_data_from_pickle_data_frame = pd.read_pickle('/Users/venkuburagadda/PycharmProjects/Regression/src/data/housing_data_seed80.pickle')
    #Loading test data from pickle
    loading_test_data_from_pickle_data_frame = pd.read_pickle('/Users/venkuburagadda/PycharmProjects/Regression/src/data/housing_data_seed20.pickle')

    #loading_data_from_pickle_data_frame['date'] = pd.to_datetime(loading_data_from_pickle_data_frame['date'])
    print('****TYpe',type(loading_data_from_pickle_data_frame['price']))
    output = np.array(loading_data_from_pickle_data_frame['price'],dtype=np.dtype)


    slope,intercept= simple_linear_regression(loading_data_from_pickle_data_frame['sqft_living'],loading_data_from_pickle_data_frame['price'])
    print('Finally',str(slope),str(intercept))
    print('Get regression', get_regression_predictions(2650,intercept,slope))
    print('RSS', get_residual_sum_of_squares(loading_data_from_pickle_data_frame['sqft_living'],loading_data_from_pickle_data_frame['price'],intercept,slope))
    slope2,intercept2 = simple_linear_regression_with_mean(loading_data_from_pickle_data_frame['sqft_living'],loading_data_from_pickle_data_frame['price'])

    test_slope,test_intercept= simple_linear_regression(loading_test_data_from_pickle_data_frame['sqft_living'],loading_test_data_from_pickle_data_frame['price'])

    print('RSS_TEST_DATA',
          get_residual_sum_of_squares(loading_test_data_from_pickle_data_frame['sqft_living'],
                                      loading_test_data_from_pickle_data_frame['price'],test_intercept,test_slope))


    # testing the model
    test_feature = np.array(range(5))
    test_output = np.array(1+1*test_feature)
    print(test_feature,test_output)
    slp, intr = simple_linear_regression(test_feature,test_output)
    print('test s',slp,'test in',intr)


def simple_linear_regression_with_mean(input_feature,output):
    x = input_feature
    y = output

    numerator = ((x*y).mean()) - (x.mean()) * (y.mean())
    denominator = ((x**2).mean()) - (x.mean())*(x.mean())
    slope = numerator/denominator


    intercept = y.mean() - slope * (x.mean())
    print("NNNNN", numerator, 'DDDDDDDDD', denominator, 'n/d', slope, 'inter', intercept)
    return slope,intercept


def simple_linear_regression(input_feature,output):
    x = input_feature #np.array(input_feature)
    y = output #np.array(output)
    total_records = x.size
    sum_of_y = y.sum()
    sum_of_x = x.sum()
    product_of_x_y = x*y
    product_of_x_y_array = np.array(product_of_x_y)
    sum_of_x_squares = ( x ** 2).sum()
    print('Stata from Simple Liner Regress',total_records,sum_of_x,sum_of_y,product_of_x_y_array.sum(),sum_of_x_squares)

    #formula to calculate w1 which is slope
    numerator = ( product_of_x_y_array.sum() - (1/total_records) * (sum_of_y * sum_of_x) )
    denominator = ( sum_of_x_squares - (1/total_records) * ((sum_of_x)  * (sum_of_x)))
    slope = numerator/denominator
    intercept = ( sum_of_y/total_records ) - slope * ( sum_of_x/total_records )

    print('numerator', numerator, 'denominator ',denominator, 'slope:', slope, 'intercept: ', intercept)


    total = []
    sum_of_x_squares_calculated = []
    for i in range(len(input_feature)):
        #print(i,':',x[i]*y[i])
        total.append(x[i]*y[i])
        sum_of_x_squares_calculated.append(x[i]**2)
    print('Sum of X*y',np.array(total).sum(),'Mean of sum x*y',np.array(total).mean())
    #print('Sum of x squared',sum_of_x_squares_calculated)
    #print('Sum of x squared SUM', np.array(sum_of_x_squares_calculated).sum())

    return slope, intercept

def get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope):
    y = sqft_intercept + sqft_slope*my_house_sqft
    return y


def get_residual_sum_of_squares(input_feature,output,intercept,slope):
    sigma_prediction = []
    for i in range(len(input_feature)):
        y = intercept + slope * output[i]
        value = (input_feature[i] - y)**2
        sigma_prediction.append(value)
    return np.array(sigma_prediction).sum()


if __name__ == '__main__':
    #test()
    pand()