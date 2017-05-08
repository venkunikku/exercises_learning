import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pand():
    dtype_dict = {'bathrooms': float, 'waterfront': int, 'sqft_above': int, 'sqft_living15': float, 'grade': int,
                  'yr_renovated': int, 'price': float, 'bedrooms': float, 'zipcode': str, 'long': float,
                  'sqft_lot15': float, 'sqft_living': float, 'floors': str, 'condition': int, 'lat': float, 'date': str,
                  'sqft_basement': int, 'yr_built': int, 'id': str, 'sqft_lot': int, 'view': int}

    # Loading data and converting to pickle
    #df = pd.read_csv('data/kc_house_train_data.csv',dtype=dtype_dict)
    #df.to_pickle('data/housing_data_seed80.pickle')

    ##df_test = pd.read_csv('/Users/venkuburagadda/iPython_Notebook_Data/Regression_Actual_Course/Week1/Quize_2/kc_house_test_data.csv')
    ##df_test.to_pickle('/Users/venkuburagadda/PycharmProjects/Regression/src/data/housing_data_seed20.pickle')

    # Loading train data from pickle.
    loading_data_from_pickle_data_frame = pd.read_pickle(
        '../data/housing_data_seed80.pickle')

    print(loading_data_from_pickle_data_frame.values)

    #writing data as a CSV
    loading_data_from_pickle_data_frame.to_csv('../data/housring_data_seed80.csv',sep=',')

    # Loading test data from pickle
    test_loading_test_data_from_pickle_data_frame = pd.read_pickle(
        '../data/housing_data_seed20.pickle')

    #saving file back to CSV
    test_loading_test_data_from_pickle_data_frame.to_csv('../data/housing_data_test_seed20.csv',sep=',')

    print(test_loading_test_data_from_pickle_data_frame.head())

    # loading_data_from_pickle_data_frame['date'] = pd.to_datetime(loading_data_from_pickle_data_frame['date'])

    train_output = loading_data_from_pickle_data_frame['price']
    train_input_feature = loading_data_from_pickle_data_frame['sqft_living']
    train_input_feature_bedrooms = loading_data_from_pickle_data_frame['bedrooms']

    test_output = test_loading_test_data_from_pickle_data_frame['price']
    test_input_feature = test_loading_test_data_from_pickle_data_frame['sqft_living']

    #print(train_input_feature.as_matrix(columns=))
    #print(train_output.columns[1:])

    #mat = np.matrix([train_input_feature.tolist(),train_output.tolist()])
    #print(mat)

    #plt.plot(train_input_feature, train_output, ".")
    #plt.show()

    train_intercept, train_slope = simple_linear_regression(train_input_feature, train_output)
    print('Intercept and Slope After Calculation', str(train_intercept), str(train_slope))

    prediction_for_sq_2650 = get_regression_predictions(2650, train_intercept, train_slope)
    print('prediction_for_sq_2650- rounded', round(prediction_for_sq_2650, 2))

    train_rss = get_residual_sum_of_squares(train_input_feature, train_output, train_intercept, train_slope)
    print('RSS- train_rss', train_rss)

    train_intercept_mean, train_slope_mean = simple_linear_regression_with_mean(train_input_feature, train_output)
    print('Intercept and Slope After Calculation using Mean', str(train_intercept_mean), str(train_slope_mean))

    test_intercept, test_slope = simple_linear_regression(test_input_feature, test_output)
    print('Test Data Intercept and Slope', str(test_intercept), str(test_slope))

    sq_ft_estimate = inverse_regression_predictions(800000, train_intercept, train_slope)
    print('Sq_ft Prediction', sq_ft_estimate)

    bedroom_intercept, bedroom_slope = simple_linear_regression(train_input_feature_bedrooms, train_output)
    print('Bedroom intercept and slope ', bedroom_intercept, bedroom_slope)
    bedroom_rss = get_residual_sum_of_squares(train_input_feature_bedrooms, train_output, bedroom_intercept,
                                              bedroom_slope)
    print('RSS bedroom -rss', bedroom_rss)

    # testing the model
    testing_feature = np.array(range(5))
    testing_output = np.array(1 + 1 * testing_feature)
    print('Testing', testing_feature, testing_output)
    testing_intr, testing_slp = simple_linear_regression(testing_feature, testing_output)
    print('test s', testing_slp, 'test in', testing_intr)

    test_rss = get_residual_sum_of_squares(testing_feature,
                                           testing_output, testing_intr, testing_slp)
    print('RSS- test_rss', test_rss)


def simple_linear_regression_with_mean(input_feature, output):
    x = input_feature
    y = output

    numerator = ((x * y).mean()) - (x.mean()) * (y.mean())
    denominator = ((x ** 2).mean()) - (x.mean()) * (x.mean())
    slope = numerator / denominator

    intercept = y.mean() - slope * (x.mean())
    print("Mean Numerator", numerator, 'Mean Denominator', denominator, 'n/d', slope, 'inter', intercept)
    return intercept, slope


def simple_linear_regression(input_feature, output):
    x = input_feature  # np.array(input_feature)
    y = output  # np.array(output)
    total_records = float((x).size)
    sum_of_y = y.sum()
    sum_of_x = x.sum()
    product_of_x_y_sum = (x * y).sum()
    print('type', type(x))
    sum_of_x_squares = (x ** 2).sum()

    print('Stata from Simple Liner Regress', total_records, sum_of_x, sum_of_y, product_of_x_y_sum, sum_of_x_squares)

    # formula to calculate w1 which is slope
    numerator = (product_of_x_y_sum - (1 / total_records) * (sum_of_y * sum_of_x))
    denominator = (sum_of_x_squares - (1 / total_records) * (sum_of_x) * (sum_of_x))

    slope = numerator / denominator

    # formula to calculate wo which is intercept
    intercept = (sum_of_y / total_records) - slope * (sum_of_x / total_records)

    # print('numerator', numerator, 'denominator ',denominator, 'slope:', slope, 'intercept: ', intercept)

    # total = []
    # sum_of_x_squares_calculated = []
    # for i in range(len(input_feature)):
    # print(i,':',x[i]*y[i])
    #    total.append(x[i]*y[i])
    #    sum_of_x_squares_calculated.append(x[i]**2)
    # print('Sum of X*y',np.array(total).sum(),'Mean of sum x*y',np.array(total).mean())
    return intercept, slope


def get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope):
    y = sqft_intercept + sqft_slope * my_house_sqft
    return y


def get_residual_sum_of_squares(input_feature, output, intercept, slope):
    sigma_prediction = []
    for i in range(len(input_feature)):
        y = intercept + slope * input_feature[i]
        value = (output[i] - y) ** 2
        sigma_prediction.append(value)

    # rss = ( input_feature - (intercept+slope*output) **2 ).sum()
    return np.array(sigma_prediction).sum()


def inverse_regression_predictions(output, intercept, slope):
    return (output - intercept) / slope


if __name__ == '__main__':
    # test()
    pand()
