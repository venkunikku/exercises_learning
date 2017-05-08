import pandas as pd
import numpy as np


def multiple_regression():
    dtype_dict = {'bathrooms': float, 'waterfront': int, 'sqft_above': int, 'sqft_living15': float, 'grade': int,
                  'yr_renovated': int, 'price': float, 'bedrooms': float, 'zipcode': str, 'long': float,
                  'sqft_lot15': float, 'sqft_living': float, 'floors': str, 'condition': int, 'lat': float, 'date': str,
                  'sqft_basement': int, 'yr_built': int, 'id': str, 'sqft_lot': int, 'view': int}
    train_data_set = pd.read_csv("../data/multi_regression/kc_house_train_data.csv", dtype=dtype_dict)
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

from math import sqrt

def regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance):
    converged = False
    weights = np.array(initial_weights)
    i = 0
    while not converged:
        i += 1
        prediction = predict_output(feature_matrix, weights)
        errors = prediction - output

        gradient_sum_squares = 0

        for i in range(len(weights)):
            derivative = feature_derivative(errors,feature_matrix[:, i])
            gradient_sum_squares += derivative**2
            weights[i] -= step_size * derivative
            print(derivative, gradient_sum_squares, i, weights[i], tolerance)
        gradient_magnitued = sqrt(gradient_sum_squares)

        if gradient_magnitued < tolerance:
            converged = True
    print("Total Iterations: ", i)
    return weights

if __name__ == '__main__':
    multiple_regression()
