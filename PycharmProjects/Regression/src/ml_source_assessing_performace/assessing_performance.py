import graphlab as gl
import matplotlib.pyplot as plt

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
    print tmp
    print tmp_cubed

    ex_sframe = gl.SFrame()
    ex_sframe['power_1'] = tmp
    print ex_sframe

    sales = gl.SFrame('../data/week3_assessing_performance_data'
                      '/Week3/Assign1/GraphLabCreate/kc_house_data.gl')

    sales = sales.sort(['sqft_living', 'price'])
    print sales
    poly1_data = polynomial_sframe(sales['sqft_living'], 15)
    poly1_data['price'] = sales['price']
    model1 = gl.linear_regression.create(poly1_data, target='price', features=['power_1'], validation_set=None)

    coef = model1.get("coefficients")
    print coef
    plt.plot(poly1_data['power_1'], poly1_data['price'], '.',
             poly1_data['power_1'], model1.predict(poly1_data), '-')

    poly2_data = polynomial_sframe(sales['sqft_living'], 2)
    my_features = poly2_data.column_names()  # get the name of the features
    poly2_data['price'] = sales['price']  # add price to the data since it's the target
    model2 = gl.linear_regression.create(poly2_data, target='price', features=my_features, validation_set=None)

    print model2.get("coefficients")

    plt.plot(poly2_data['power_1'], poly2_data['price'], '.',
             poly2_data['power_1'], model2.predict(poly2_data), '-')

    plt.show()

if __name__ == '__main__':
    cubing_using_graphlab()
    polynomial_regression()
