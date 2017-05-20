import graphlab as gl
import matplotlib.pyplot as plt
from math import sqrt

def polynomial_regression():
    pass


def polynomial_sframe(feature, degree):
    poly_sframe = gl.SFrame()
    poly_sframe['power_1'] = feature

    if degree > 1:
        for power in range(2, degree+1):
            name = 'power_' + str(power)
            tmp = gl.SArray(feature)
            tmp_power = tmp.apply(lambda x: x**power)
            poly_sframe[name] = tmp_power

    #print poly_sframe
    return poly_sframe




def cubing_using_graphlab():
    tmp = gl.SArray([1.,2.,3.])
    tmp_cubed = tmp.apply(lambda x: x**3)
    #print tmp
    #print tmp_cubed

    ex_sframe = gl.SFrame()
    ex_sframe['power_1'] = tmp
    #print ex_sframe

    sales = gl.SFrame('../data/week3_assessing_performance_data'
                      '/Week3/Assign1/GraphLabCreate/kc_house_data.gl')

    sales = sales.sort(['sqft_living', 'price'])
    #print sales

    # DEGRESS !
    poly1_data = polynomial_sframe(sales['sqft_living'], 1)
    poly1_data['price'] = sales['price']
    model1 = gl.linear_regression.create(poly1_data, target='price', features=['power_1'], validation_set=None)

    coef = model1.get("coefficients")
    print '**************Degree-1 Coefficients***********'
    print coef
    print '**********************************************'

    fig1 = plt.figure("Degree 1 Graph")
    axis1 = fig1.add_subplot(111)

    axis1.plot(poly1_data['power_1'], poly1_data['price'], '.',
             poly1_data['power_1'], model1.predict(poly1_data), '-')



    #DEGRESS -2
    poly2_data = polynomial_sframe(sales['sqft_living'], 2)
    poly2_features = poly2_data.column_names()
    poly2_data['price'] = sales['price']
    model2 = gl.linear_regression.create(poly2_data, target='price', features=poly2_features, validation_set=None)
    print '**************Degree-2 Coefficients***********'
    print model2.get('coefficients')
    print '**********************************************'

    fig2 = plt.figure("DEGREE-2")
    axis2 = fig2.add_subplot(111)
    axis2.plot(poly2_data['power_1'], poly2_data['price'], '.',
               poly2_data['power_1'],model2.predict(poly2_data),'-')

    #print poly2_data


    poly3_data = polynomial_sframe(sales['sqft_living'],3)
    poly3_features = poly3_data.column_names()
    poly3_data['price'] = sales['price']
    model3 = gl.linear_regression.create(poly3_data,target='price',features=poly3_features, validation_set=None)
    print '**************Degree-3 Coefficients***********'
    print model3.get('coefficients')
    print '**********************************************'

    fig3 = plt.figure("DEGREE - 3")
    axis3 = fig3.add_subplot(111)
    axis3.plot(poly3_data['power_1'], poly3_data['price'], '.',
               poly3_data['power_1'],model3.predict(poly2_data),'-')


    poly2_data = polynomial_sframe(sales['sqft_living'], 15)
    my_features = poly2_data.column_names()  # get the name of the features
    poly2_data['price'] = sales['price']  # add price to the data since it's the target
    model2 = gl.linear_regression.create(poly2_data, target='price', features=my_features, validation_set=None)
    print '**************Degree-15 Coefficients***********'
    print model2.get("coefficients").print_rows(num_rows=16)
    print '**********************************************'

    fig22 = plt.figure("Degree 16 Graph")
    axis22 = fig22.add_subplot(111)
    axis22.plot(poly2_data['power_1'], poly2_data['price'], '.',
             poly2_data['power_1'], model2.predict(poly2_data), '-')


    ####################################################################################################################

    sales2 = gl.SFrame('../data/week3_assessing_performance_data'
                      '/Week3/Assign1/GraphLabCreate/kc_house_data.gl')
    initial_split1,initial_split2 = sales2.random_split(0.5, seed=0)

    set_1, set_2 = initial_split1.random_split(0.5,seed=0)
    set_3, set_4 = initial_split2.random_split(0.5, seed=0)

    set_1_data = polynomial_sframe(set_1['sqft_living'], 15)
    set_1_feature = set_1_data.column_names()
    set_1_data['price'] = set_1['price']
    model_set_1 = gl.linear_regression.create(set_1_data,target='price', features=set_1_feature, validation_set=None)
    print '**************SET_1-15 Coefficients***********'
    print model_set_1.get("coefficients").print_rows(num_rows=17)
    print '****'*30

    fig_set_1 = plt.figure('SET_1 - 15')
    axis_set_1 = fig_set_1.add_subplot(111)
    axis_set_1.plot(set_1_data['power_1'],set_1_data['price'],'.',
                   set_1_data['power_1'], model_set_1.predict(set_1_data), '-')


    set_2_data = polynomial_sframe(set_2['sqft_living'], 15)
    set_2_feature = set_2_data.column_names()
    set_2_data['price'] = set_2['price']
    model_set_2 = gl.linear_regression.create(set_2_data, target='price', features=set_2_feature, validation_set=None)
    print '**************SET_2-15 Coefficients***********'
    print model_set_2.get("coefficients").print_rows(num_rows=17)
    print '****' * 30

    fig_set_2 = plt.figure('SET_2 - 15')
    axis_set_2 = fig_set_2.add_subplot(111)
    axis_set_2.plot(set_2_data['power_1'], set_2_data['price'], '.',
                    set_2_data['power_1'], model_set_2.predict(set_2_data), '-')


    set_3_data = polynomial_sframe(set_3['sqft_living'], 15)
    set_3_feature = set_3_data.column_names()
    set_3_data['price'] = set_3['price']
    model_set_3 = gl.linear_regression.create(set_3_data, target='price', features=set_3_feature, validation_set=None)
    print '**************SET_3-15 Coefficients***********'
    print model_set_3.get("coefficients").print_rows(num_rows=17)
    print '****' * 30

    fig_set_3 = plt.figure('SET_3 - 15')
    axis_set_3 = fig_set_3.add_subplot(111)
    axis_set_3.plot(set_3_data['power_1'], set_3_data['price'], '.',
                    set_3_data['power_1'], model_set_3.predict(set_3_data), '-')

    set_4_data = polynomial_sframe(set_4['sqft_living'], 15)
    set_4_feature = set_4_data.column_names()
    set_4_data['price'] = set_4['price']
    model_set_4 = gl.linear_regression.create(set_4_data, target='price', features=set_4_feature, validation_set=None)
    print '**************SET_4-15 Coefficients***********'
    print model_set_4.get("coefficients").print_rows(num_rows=17)
    print '****' * 30

    fig_set_4 = plt.figure('SET_4 - 15')
    axis_set_4 = fig_set_4.add_subplot(111)
    axis_set_4.plot(set_4_data['power_1'], set_4_data['price'], '.',
                    set_4_data['power_1'], model_set_4.predict(set_4_data), '-')

    ##################################################################################################################

    sales3 = gl.SFrame('../data/week3_assessing_performance_data'
                       '/Week3/Assign1/GraphLabCreate/kc_house_data.gl')
    training_and_validation, testing = sales3.random_split(0.9, seed=1)
    training, validation = training_and_validation.random_split(0.5, seed=1)

    all_valiation_set_rss = []
    all_test_set_rss = []
    for deg in range(1, 16):
        poly_data = polynomial_sframe(training['sqft_living'],deg)
        my_features = poly_data.column_names()
        poly_data['price'] = training['price']
        model = gl.linear_regression.create(poly_data,target='price', features=my_features, validation_set=None, verbose=False)
        poly_validation_data = polynomial_sframe(validation['sqft_living'], deg)
        poly_validation_data['price'] = validation['price']
        predicted_price = model.predict(poly_validation_data)
        error = validation['price'] - predicted_price
        error_squared = error**2
        root_mean_squared = error_squared.sum()
        all_valiation_set_rss.append((sqrt(root_mean_squared),deg))

        poly_test_data = polynomial_sframe(testing['sqft_living'], deg)
        poly_test_data['price'] = testing['price']
        test_prediction_price = model.predict(poly_test_data)
        error_test = testing['price']-test_prediction_price
        error_test_sqrared = error_test**2
        error_test_sum = error_test_sqrared.sum()
        all_test_set_rss.append((sqrt(error_test_sum),deg))

    all_valiation_set_rss.sort()
    all_test_set_rss.sort()

    for i, each_rss in enumerate(all_valiation_set_rss):
        print i, each_rss

    print '***'*25

    for i,data in enumerate(all_test_set_rss):
        print i, data

    #plt.show()

if __name__ == '__main__':
    cubing_using_graphlab()
    polynomial_regression()





