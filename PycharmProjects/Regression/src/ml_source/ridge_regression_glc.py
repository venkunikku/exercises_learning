import graphlab as gl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import sqrt


def polynomial_sframe(feature, degree):
    poly_sfram = gl.SFrame()
    # we will get only 1 feature so
    poly_sfram['power_1'] = feature

    if degree > 1:
        for i in range(2, degree + 1):
            tmp = gl.SArray(feature)
            multipllied = tmp.apply(lambda x: x ** i)
            poly_sfram['power_' + str(i)] = multipllied
    return poly_sfram


def ridge_regression():
    sales = gl.SFrame('../data/week4_ridge_regression/kc_house_data.gl')
    sales = sales.sort(['sqft_living', 'price'])

    l2_small_penality = 1e-5
    poly_data = polynomial_sframe(sales['sqft_living'], 15)
    my_feature = poly_data.column_names()
    poly_data['price'] = sales['price']
    poly_model = gl.linear_regression.create(poly_data, target='price',
                                             features=my_feature,
                                             l2_penalty=l2_small_penality,
                                             validation_set=None)
    print(poly_model['coefficients'])

    fig1 = plt.figure("Degree 1 Graph- rigid regression")
    axis1 = fig1.add_subplot(111)

    axis1.plot(poly_data['power_1'], poly_data['price'], '.',
               poly_data['power_1'], poly_model.predict(poly_data), '-')

    print("**" * 30)

    # Vary this penality to try different models and plots
    # l2_small_penality = 1e-5 # got differnet fits for each of the sets below.
    l2_small_penality = 1e5

    (semi_split1, semi_split2) = sales.random_split(.5, seed=0)
    (set_1, set_2) = semi_split1.random_split(0.5, seed=0)
    (set_3, set_4) = semi_split2.random_split(0.5, seed=0)

    # set1
    print("*************set1*************************************************")
    poly_data_set1 = polynomial_sframe(set_1['sqft_living'], 15)
    set1_my_feature = poly_data_set1.column_names()
    poly_data_set1['price'] = set_1['price']
    set1_model = gl.linear_regression.create(poly_data_set1, target='price',
                                             features=set1_my_feature,
                                             l2_penalty=l2_small_penality,
                                             validation_set=None)

    print(set1_model['coefficients'])

    fig2 = plt.figure("SET-1- rigid regression")
    axis2 = fig2.add_subplot(111)

    axis2.plot(poly_data_set1['power_1'], poly_data_set1['price'], '.',
               poly_data_set1['power_1'], set1_model.predict(poly_data_set1), '-')

    print("*************set1********************************************End")

    # set2
    print("*************set2*************************************************")
    poly_data_set2 = polynomial_sframe(set_2['sqft_living'], 15)
    set2_my_feature = poly_data_set2.column_names()
    poly_data_set2['price'] = set_2['price']
    set2_model = gl.linear_regression.create(poly_data_set2, target='price',
                                             features=set2_my_feature,
                                             l2_penalty=l2_small_penality,
                                             validation_set=None)

    print(set2_model['coefficients'])

    fig3 = plt.figure("SET-2- rigid regression")
    axis3 = fig3.add_subplot(111)

    axis3.plot(poly_data_set2['power_1'], poly_data_set2['price'], '.',
               poly_data_set2['power_1'], set2_model.predict(poly_data_set2), '-')

    print("*************set2********************************************End")

    # set3
    print("*************set3*************************************************")
    poly_data_set3 = polynomial_sframe(set_3['sqft_living'], 15)
    set3_my_feature = poly_data_set3.column_names()
    poly_data_set3['price'] = set_3['price']
    set3_model = gl.linear_regression.create(poly_data_set3, target='price',
                                             features=set3_my_feature,
                                             l2_penalty=l2_small_penality,
                                             validation_set=None)

    print(set3_model['coefficients'])

    fig4 = plt.figure("SET-3- rigid regression")
    axis4 = fig4.add_subplot(111)

    axis4.plot(poly_data_set3['power_1'], poly_data_set3['price'], '.',
               poly_data_set3['power_1'], set3_model.predict(poly_data_set3), '-')

    print("*************set3********************************************End")

    # set4
    print("*************set3*************************************************")
    poly_data_set4 = polynomial_sframe(set_4['sqft_living'], 15)
    set4_my_feature = poly_data_set4.column_names()
    poly_data_set4['price'] = set_4['price']
    set4_model = gl.linear_regression.create(poly_data_set4, target='price',
                                             features=set4_my_feature,
                                             l2_penalty=l2_small_penality,
                                             validation_set=None)

    print(set4_model['coefficients'])

    fig5 = plt.figure("SET-4- rigid regression")
    axis5 = fig5.add_subplot(111)

    axis5.plot(poly_data_set4['power_1'], poly_data_set4['price'], '.',
               poly_data_set4['power_1'], set4_model.predict(poly_data_set4), '-')

    print("*************set4********************************************End")


    print('*********************k-Fold*****degree-15**************************')
    sales = gl.SFrame('../data/week4_ridge_regression/kc_house_data.gl')
    sales = sales.sort(['sqft_living', 'price'])
    (train_valid, test) = sales.random_split(.9, seed=1)
    train_valid_shuffled = gl.toolkits.cross_validation.shuffle(train_valid, random_seed=1)

    total_rows = len(train_valid_shuffled)
    kfold = 10
    poly_on_shuffled_data = polynomial_sframe(train_valid_shuffled['sqft_living'], 15)
    my_features_shuffled = poly_on_shuffled_data.column_names()
    poly_on_shuffled_data['price'] = train_valid_shuffled['price']

    details = []
    for penality in np.logspace(1, 7, num=13):
        print("*********Working On Following Penality******: ", penality)
        results = []
        avg_mean = k_fold_cross_validation(10,penality,poly_on_shuffled_data,
                                'price',my_features_shuffled )

        details.append((penality,avg_mean))

    only_avg = []
    for i in details:
        print( i[0], ' ******** ', i[1] )
        only_avg.append(i[1])

    final_model = gl.linear_regression.create(poly_on_shuffled_data,target='price'
                                              ,features=my_features_shuffled,
                                 l2_penalty=1000,validation_set=None,verbose=True)
    test_predicted_value = final_model.predict(test)
    test_difference = test['price'] - test_predicted_value
    squred_test_difference = test_difference**2
    print(sum(squred_test_difference))

    fig6= plt.figure("SET-5- rigid regression with Penality")
    axis6 = fig6.add_subplot(111)

    axis6.plot(np.logspace(1, 7, num=13),only_avg,'.' )
    plt.xscale('log')

    only_avg.sort()
    print(only_avg)
    plt.show()

def k_fold_cross_validation(k, l2_penalty, data, output_name, features_list):
    total_rows = len(data)
    results = []

    for i in range(k):
        print("****Penality:", l2_penalty, " *****Kfold:", i)
        start, end = get_start_end_index(total_rows, k, i)
        validation_set = data[start:end + 1]
        training_start_slice = data[0: start]
        training_end_slice = data[end + 1:total_rows]
        train_set_appended = training_start_slice.append(training_end_slice)
        model = gl.linear_regression.create(train_set_appended, target=output_name,
                                            features=features_list
                                            , l2_penalty=l2_penalty, validation_set=None,
                                            verbose=False)
        predict = model.predict(validation_set)

        difference_in_prediction = validation_set['price'] - predict
        difference_in_prediction_sqr = difference_in_prediction ** 2
        sum_of_difference = difference_in_prediction_sqr.sum()
        square_root_of_prediction = sqrt(sum_of_difference)
        results.append(square_root_of_prediction)

    all_value = gl.SArray(results)
    mean = all_value.mean()
    return mean


def k_fold():
    print('*********************k-Fold*****degree-15**************************')

    sales = gl.SFrame('../data/week4_ridge_regression/kc_house_data.gl')
    sales = sales.sort(['sqft_living', 'price'])
    (train_valid, test) = sales.random_split(.9, seed=1)
    train_valid_shuffled = gl.toolkits.cross_validation.shuffle(train_valid, random_seed=1)

    total_rows = len(train_valid_shuffled)
    kfold = 10
    poly_on_shuffled_data = polynomial_sframe(train_valid_shuffled['sqft_living'], 15)
    my_features_shuffled = poly_on_shuffled_data.column_names()
    poly_on_shuffled_data['price'] = train_valid_shuffled['price']

    details = []
    for penality in np.logspace(1, 7, num=13):
        print("*********Working On Following Penality******: ", penality)
        results = []
        for i in range(kfold + 1):
            print("****Penality:", penality, " *****Kfold:", i)
            start, end = get_start_end_index(total_rows, kfold, i)
            validation_set = poly_on_shuffled_data[start:end + 1]
            training_start_slice = poly_on_shuffled_data[0: start]
            training_end_slice = poly_on_shuffled_data[end + 1:total_rows]
            train_set_appended = training_start_slice.append(training_end_slice)
            model = gl.linear_regression.create(train_set_appended, target='price',
                                                features=my_features_shuffled
                                                , l2_penalty=penality, validation_set=None)
            predict = model.predict(validation_set)

            difference_in_prediction = validation_set['price'] - predict
            difference_in_prediction_sqr = difference_in_prediction**2
            sum_of_difference = difference_in_prediction_sqr.sum()

            square_root_of_prediction = sqrt(sum_of_difference)
            results.append(square_root_of_prediction)

        all_value = gl.SArray(results)
        mean = all_value.mean()
        dtails = (penality, mean)
        details.append(dtails)

def get_start_end_index(total_length_of_data, k_fold, i):
    n = total_length_of_data
    k = k_fold  # 10-fold cross-validation
    start = (n * i) / k
    end = (n * (i + 1)) / k - 1
    print i, (start, end)
    return (start, end)

def test():
    print(10**1.5)
    print(np.array([10**1.5]))

if __name__ == '__main__':
    ridge_regression()
    #k_fold()
    #test()
