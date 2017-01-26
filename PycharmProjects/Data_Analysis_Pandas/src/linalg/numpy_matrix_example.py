import numpy as np
def test():
    mat = np.matrix('1 0 ; 0 1 ')
    print(mat)

    mat2 = np.matrix([[1,2],[1,2]])
    print(mat2)

    print(mat2*mat)

    twobythree = np.matrix('1 2 3 ; 4 5 6')
    threebytwo = np.matrix('7 8 ; 9 10 ; 11 12')

    print(twobythree)
    print(threebytwo)

    print(twobythree*threebytwo)

    squarematrix = [[1,2],[3,4]]

    # finding determinante
    determinante = np.linalg.det(squarematrix)
    print(determinante)

    # for larger matrices you have to use slogdet and then find the log to get det
    sign,logdet = np.linalg.slogdet(squarematrix)
    print('Sign and logdetails', sign, logdet)
    final_determinant = sign * np.exp(logdet)
    print('final det', final_determinant)

    # identity matrix of 4X4
    print(np.eye(4))
    # a 1X1 matrix with all 1's
    print(np.ones(4,))
    # a 1x1 matrix of all 0's
    print(np.zeros(4))

    #Rank of a matrix
    print('matrix rank:',np.linalg.matrix_rank(squarematrix))

    print('matrix null space', )

if __name__ == '__main__':
    test()