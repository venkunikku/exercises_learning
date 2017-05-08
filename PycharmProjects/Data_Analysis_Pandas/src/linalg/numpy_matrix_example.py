import numpy as np
from scipy import linalg as LA
import numpy.linalg as n_LA
import pandas as pa
import sympy as symp




def test():
    exercise4_2 = np.matrix('1 0 ; 0 1 ')
    print(exercise4_2)

    mat2 = np.matrix([[1, 2], [1, 2]])
    print(mat2)

    print(mat2 * exercise4_2)

    twobythree = np.matrix('1 2 3 ; 4 5 6')
    threebytwo = np.matrix('7 8 ; 9 10 ; 11 12')

    print(twobythree)
    print(threebytwo)

    print(twobythree * threebytwo)

    squarematrix = [[1, 2], [3, 4]]

    # finding determinante
    determinante = np.linalg.det(squarematrix)
    print(determinante)

    # for larger matrices you have to use slogdet and then find the log to get det
    sign, logdet = np.linalg.slogdet(squarematrix)
    print('Sign and logdetails', sign, logdet)
    final_determinant = sign * np.exp(logdet)
    print('final det', final_determinant)

    # identity matrix of 4X4
    print(np.eye(4))
    # a 1X1 matrix with all 1's
    print(np.ones(4, ))
    # a 1x1 matrix of all 0's
    print(np.zeros(4))

    # Rank of a matrix
    print('matrix rank:', np.linalg.matrix_rank(squarematrix))

    print('matrix null space', )

    random_matrix = np.random.rand(5, 5)
    print('random matxi float', random_matrix)

    random_ints = np.random.random_integers(0, 100, (5, 5))
    A = np.random.randint(0, 10, 25).reshape(5, 5)
    print('Random matrix intergers', random_ints)
    print('NUmpy Random Inds', A)

    print('finding eigen values and eignen vectors')

    e_vals, e_vectors = LA.eig(random_ints)
    print(e_vals)
    print(e_vectors)

    exercise4_2 = [[1, 2], [4, 3]]
    np_sq_matix = np.matrix(exercise4_2)

    e_v, e_ve = LA.eig(exercise4_2)
    print('exercise4_2', e_v)
    print('exercise4_2', e_ve)
    print('Real Part****',e_v[0].real)
    print('Imaginary Part****', e_v[0].imag)

    print(np_sq_matix)
    print(LA.eig(np_sq_matix))

    exercise4_3 = [[7, 1, -2], [-3, 3, 6], [2, 2, 2]]
    print('exercise4_3:', LA.eig(exercise4_3))

    mat2 = [[1, 1], [1, 0]]
    e_value, e_vect = LA.eig(mat2)
    print(e_value, e_vect)
    print(e_value[0])
    print('ONly Eigin values', LA.eigvals(mat2))
    print()

    exercise4_1 = np.matrix([[3, 1], [1, 3]])
    print('Eigne Value and Vectors:', LA.eig(exercise4_1))

    exercise4_4 = np.matrix([[1, 0], [0, -1]])
    print('exercise4_4', LA.eig(exercise4_4))
    print('one values', type(LA.eig(exercise4_4)[0][0]))
    print(1 % 3)

    exercise4_8 = np.matrix([[5, -3, 2], [1, 0, 2], [2, -1, 3]])
    # exercise4_8 = np.matrix([[5, -3, 2,3], [1, 0, 2,4], [2, -1, 3,5], [1, 2, 3,6]])
    print("Determinanted : ", LA.det(exercise4_8))

    exercice4_14_1 = np.matrix([[2, 1], [2, 3]])
    exercice4_14_2 = np.matrix([[5, 1], [2, 1]])
    multi = exercice4_14_1 * exercice4_14_2
    print('multiplication', multi)
    print('Determinant', LA.det(multi))

    lewis_carroll = np.matrix(
        [
            [2, 3, -1, 2, 0],
            [1, 2, 3, 1, 4],
            [2, -1, 2, 1, 1],
            [3, 1, -1, 2, -2],
            [-4, 1, 0, 1, 2],

        ]

    )
    print('Deter', LA.det(lewis_carroll))

    exercise4_21 = np.matrix(
        [[0, 1],
         [2, 1]

         ]
    )

    exercise4_21_2 = np.matrix([[5], [1]])
    print('exercise4_21: ', LA.eig(exercise4_21))

    print((exercise4_21 ** 10) * exercise4_21_2)

    exercise4_24_a = np.matrix([[1,3],[2,2]])
    ignv,ignve = LA.eig(exercise4_24_a)
    inverser_of_eignen = n_LA.inv(ignve)

    print('Eigen vector',ignve)
    print('Inverse of eigne vector',inverser_of_eignen)
    print('Eigen values',ignv)

    print('Diagonalize',inverser_of_eignen * exercise4_24_a * ignve)

    print(2.05/0.99)
    print(lewis_carroll)
    print(lewis_carroll.transpose())
    print(lewis_carroll.transpose() == lewis_carroll)
    print(lewis_carroll.transpose()*lewis_carroll)

    singular_matrix = np.matrix([[1, 0, 0], [-2, 0, 0], [4, 6, 1]])
    print(LA.det(singular_matrix))

    #reduced = np.matrix([[1,2,1,2],[3,8,1,2],[0,4,1,2]])
    #print(symp.matrix(reduced).rref())

    non_indep = np.matrix([[2,4],[6,12]])
    print('Eign values of dependent matrix',LA.eig(non_indep))

    dependent_matrix = np.matrix([[1,2,3],[1,2,3],[2,5,8]])
    try:
        print(n_LA.inv(dependent_matrix))
    except Exception as e:
        print("Singular Matrix. Inverse is not possible")

    symmetric_matrix = np.matrix([
                        [0,1],
                        [1,0],


                                  ])
    print(n_LA.inv(symmetric_matrix))
    eigvalue,eigvector = LA.eig(symmetric_matrix)
    print('eig values',eigvalue.real)
    print('Eig Vectors', eigvector)
    print('Eigen vector inverse', n_LA.inv(eigvector))
    diagonalize = n_LA.inv(eigvector) * symmetric_matrix * eigvector
    print('Diagonal', diagonalize  )

    svd_matrix = np.matrix([[0, 1, 0, 0],
                            [0, 0, 2, 0],
                            [0, 0, 0, 3],
                            [0, 0, 0, 0],
                            ])

    e_val, e_vec = LA.eigh(svd_matrix)
    print("*****************")
    print(e_vals)
    print("******")
    print(e_vec)

    svd_matrix = np.matrix([[0, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 4, 0],
                            [0, 0, 0, 9],
                            ])
    print(LA.eigh(svd_matrix))

if __name__ == '__main__':
    test()
