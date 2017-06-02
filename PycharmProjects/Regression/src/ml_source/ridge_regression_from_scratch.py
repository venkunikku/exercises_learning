import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_numpy_data(data_frame, features, output):
    data_frame['constant'] = 1
    features = ['constant'] + features
    featured_dataframe = data_frame[features]
    output_array = np.array(output)
    featured_matrix = np.array(featured_dataframe)

    return featured_matrix, output_array


def predict_output(feature_matrix, weights):
    return np.dot(feature_matrix, weights)

# this one is not required
def feature_derivative(error, feature):
    dot_product = np.dot(error, feature)
    return 2 * dot_product

def feature_derivative_ridge(errors, feature, weight, l2_penalty, feature_is_constant):
    print feature_is_constant
    if feature_is_constant:
        dot_product = np.dot(errors, feature)
        return 2*dot_product
    else :
        return np.dot(errors, feature)*2 + 2*(l2_penalty*weight) #


def ridge_regression_gradient_descent(feature_matrix, output, initial_weights,
                                      step_size, l2_penality, max_iteration=100):

    weights = np.array(initial_weights)

    j = 0
    while j < max_iteration:

        predicted_output = predict_output(feature_matrix, weights)
        errors =  predicted_output - output
        print 'working on following i: ' + str(j)
        j = j + 1
        for i in xrange(len(weights)):
            feature_is_constant = False
            if i==0:
                feature_is_constant = True

            derivative_of_the_feature = feature_derivative_ridge(errors,feature_matrix[:,i],
                                                weights[i],l2_penality,feature_is_constant)
            weights[i] -= step_size * derivative_of_the_feature
    return weights

def test():
    dtype_dict = {'bathrooms': float, 'waterfront': int, 'sqft_above': int, 'sqft_living15': float, 'grade': int,
                  'yr_renovated': int, 'price': float, 'bedrooms': float, 'zipcode': str, 'long': float,
                  'sqft_lot15': float, 'sqft_living': float, 'floors': str, 'condition': int, 'lat': float, 'date': str,
                  'sqft_basement': int, 'yr_built': int, 'id': str, 'sqft_lot': int, 'view': int}
    all_data = pd.read_csv('../data/week4_ridge_regression/quiz2/kc_house_data.csv',dtype= dtype_dict)
    train_data = pd.read_csv('../data/week4_ridge_regression/quiz2/kc_house_train_data.csv',dtype= dtype_dict)
    test_data = pd.read_csv('../data/week4_ridge_regression/quiz2/kc_house_test_data.csv',dtype= dtype_dict)

    feature_matrix, output = get_numpy_data(all_data, ['sqft_living'], all_data['price'])
    my_weights = np.array([1.,10.])
    test_prediction = predict_output(feature_matrix, my_weights)
    errors = all_data['price']-test_prediction

    print feature_derivative_ridge(errors,feature_matrix[:, 1], my_weights[1],1,False)
    print np.sum(errors*feature_matrix[:,1])*2+20.

    print feature_derivative_ridge(errors, feature_matrix[:,0],my_weights[0],1,True)
    print np.sum(errors)*2

    # Simple feature test
    simple_features = ['sqft_living']
    my_output = 'price'
    simple_feature_matrix, output = get_numpy_data(train_data, simple_features, train_data['price'])
    simple_test_feature_matrix, test_output = get_numpy_data(test_data, simple_features, test_data['price'])


    step_size = 1e-12
    max_itermation = 1000
    initial_weights = [0.,0.]
    simple_weights_0_penality = ridge_regression_gradient_descent(simple_feature_matrix, train_data['price'],
                                                                  initial_weights,step_size,0.0,max_itermation)


    simple_weights_high_penality = ridge_regression_gradient_descent(simple_feature_matrix, train_data['price'],
                                                                  initial_weights, step_size, 1e11, max_itermation)

    print "0", simple_weights_0_penality
    print "High:", simple_weights_high_penality

    plt.plot(simple_feature_matrix, output, 'k.',
             simple_feature_matrix, predict_output(simple_feature_matrix, simple_weights_0_penality), 'b-',
             simple_feature_matrix, predict_output(simple_feature_matrix, simple_weights_high_penality), 'r-')
    plt.show()

if __name__ =='__main__':
    test()