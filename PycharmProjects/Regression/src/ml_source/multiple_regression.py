import pandas as pd
import numpy as np
from math import sqrt
from math import log

def multiple_regression():
    dtype_dict = {'bathrooms': float, 'waterfront': int, 'sqft_above': int, 'sqft_living15': float, 'grade': int,
                  'yr_renovated': int, 'price': float, 'bedrooms': float, 'zipcode': str, 'long': float,
                  'sqft_lot15': float, 'sqft_living': float, 'floors': str, 'condition': int, 'lat': float, 'date': str,
                  'sqft_basement': int, 'yr_built': int, 'id': str, 'sqft_lot': int, 'view': int}
    train_data_set = pd.read_csv("../data/multi_regression/kc_house_train_data.csv", dtype=dtype_dict)

    # Adding log of sqlft
    train_data_set['log_sqft_living'] = train_data_set['sqft_living'].map(lambda x : log(x))
    train_data_set['log_sqft_living15'] = train_data_set['sqft_living15'].map(lambda x: log(x))
    train_data_set['log_price'] = train_data_set['price'].map(lambda x: log(x))
    print(train_data_set.head())

    features = ['sqft_living']
    featured_matrix, output_array = get_numpy_data(train_data_set, features, train_data_set['price'])
    print(featured_matrix[0, :])
    print(output_array[0])

    example_weights = np.array([1., 1.])
    my_features = featured_matrix[1, ]  # first data point
    print(predict_output(my_features, example_weights))

    my_weights = np.array([0., 0.])
    test_prediction = predict_output(featured_matrix, my_weights)
    errors = test_prediction - output_array
    test_feature = featured_matrix[:, 0]  # all rows but only 'constant' column
    derivative = feature_derivative(errors, test_feature)
    print(derivative)
    print(-np.sum(output_array) * 2)

    initial_weights = np.array([-47000., 1.])
    step_size = 7e-12
    tolerance = 2.5e7

    weights = regression_gradient_descent(featured_matrix, output_array, initial_weights, step_size, tolerance)
    print(weights)
    print('Rounded Weights:', round(weights[1],1))

    test_data_set = pd.read_csv("../data/multi_regression/kc_house_test_data.csv", dtype=dtype_dict)
    test_simple_feature_matrix, test_output = get_numpy_data(test_data_set, features, test_data_set['price'])
    test_data_prediction = predict_output(test_simple_feature_matrix, weights)
    print('House price of the first house',round(test_data_prediction[0]))

    errors_test_data = test_output - test_data_prediction
    print('Simple RSS on Test Data:',sqrt(errors_test_data.sum()))

    #multiple regression
    multi_feature = ['sqft_living', 'sqft_living15']
    my_output =['price']
    multi_feature_matrix,multi_output_price = get_numpy_data(train_data_set,multi_feature, train_data_set['price'])
    initila_weights = np.array([-100000., 1., 1.])
    set_size = 4e-12
    tolerance = 1e9
    multi_weights = regression_gradient_descent(multi_feature_matrix, multi_output_price, initila_weights, set_size, tolerance)
    print('Multi Weights:', multi_weights)

    print('**********************Experiment**********************************************************************')
    print('******************************************************************************************************')

    experiment_features = ['log_sqft_living','log_sqft_living15']
    exp_feature_matrix, exp_output = get_numpy_data(train_data_set,experiment_features, train_data_set['log_price'])
    initila_weights = np.array([-10., 1., 1.])
    set_size = 4e-12
    tolerance = 1e9
    exp_weights = regression_gradient_descent(exp_feature_matrix, exp_output, initila_weights,set_size,tolerance)
    print('Experiment initial weights', exp_weights)

    # doubling a colum
    print('******************************************************************************************************')
    print('Before',exp_feature_matrix)
    exp_feature_matrix[:,1] *= 2
    print('After', exp_feature_matrix)
    #initila_weights = np.array([-1000000., 1., 1.])
    #set_size = 4e-12
    #tolerance = 1e9
    double_one_weight = regression_gradient_descent(exp_feature_matrix, exp_output, initila_weights,set_size,tolerance)
    print('******************************************************************************************************')
    print('Multi Weights * 2 :', double_one_weight)

    print('******************************************************************')

    test_multi_feature_matrix, test_multi_output = get_numpy_data(test_data_set, multi_feature, test_data_set['price'])
    test_multi_prediction = predict_output(test_multi_feature_matrix, multi_weights)
    print('Multiple Regression House Price predict', round(test_multi_prediction[0]))
    print('Actual Price in the test data set:', test_data_set['price'][0])

    test_multi_errors = test_multi_output - test_multi_prediction
    print('Multi Test RSS: ', sqrt(test_multi_errors.sum()))

def get_numpy_data(data_frame, features, output):
    data_frame['constant'] = 1
    features = ['constant'] + features
    featured_dataframe = data_frame[features]
    output_array = np.array(output)
    featured_matrix = np.array(featured_dataframe)

    return featured_matrix, output_array


def predict_output(feature_matrix, weights):
    # example_weights = np.array([1., 1.])
    # my_features = featured_matrix[1,]  # first data point
    # predicted_values = np.dot(my_features, example_weights)
    # print(predicted_values)
    return np.dot(feature_matrix, weights)


def feature_derivative(error, feature):
    dot_product = np.dot(error, feature)
    return 2 * dot_product



def regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance):
    converged = False
    weights = np.array(initial_weights)
    iter = 0
    while not converged:
        iter += 1
        prediction = predict_output(feature_matrix, weights) # (HW) - (feature_matrix * weights)
        errors = prediction - output #  (y- HW)  (Actual-Estimated)

        gradient_sum_squares = 0

        for i in range(len(weights)):
            derivative = feature_derivative(errors, feature_matrix[:, i])  # final derivative for the weight.
                                                                       # derivative = (error)*Feature[i].
                                                                       # This one is for every row in the data set

            print('Derivative: ', derivative)
            #print(i, derivative)
            gradient_sum_squares += derivative**2  # here after the calcuation using W(t) t- iterations.
                                                   # Square the the values to sum
            weights[i] -= step_size * derivative  # add step size to the derivative so that it
                                                  #  can move to next point in the curve.
                                                  #  Also update the wieghts
            #print(derivative, gradient_sum_squares, i, weights[i], tolerance)
        gradient_magnitued = sqrt(gradient_sum_squares)  # RSS SQR(Sum)

        if gradient_magnitued < tolerance:
            converged = True
        else:
            #print("INSIDE", i)
            pass

    print("Total Iterations: ", iter)
    return weights

if __name__ == '__main__':
    multiple_regression()
