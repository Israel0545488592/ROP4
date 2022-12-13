import numpy as np
import numpy.random as rnd
import cvxpy as cvx

from time import perf_counter
import doctest

from typing import Tuple


def GenRanLinSys(size: int) -> np.ndarray:
    '''
    random linear equations system
    
    >>> import numpy.random as rnd
    >>> rnd.seed(1)
    >>> for n, (right, left) in zip(range(3), GenRanLinSys(2)): print(right, left)
    [[-16.59559906  44.06489869]
     [-99.97712504 -39.53348547]] [-70.64882184 -81.53228105]
    [[-62.74795772 -30.88785459]
     [-20.64650515   7.7633468 ]] [-16.16109712  37.04390008]
    [[-59.10955005  75.62348728]
     [-94.52248136  34.09350204]] [-16.53903953  11.73796569]
    '''

    if size <= 0: raise ValueError("dimentions must be posetive")

    while True:
        # making a squre matrix so there would be 1 unique solution
        yield rnd.uniform(-100, 100, (size, size)), rnd.uniform(-100, 100, size)


def CVXbuild(right: np.ndarray, left: np.ndarray) -> cvx.Problem:

    '''Building the linear program'''

    vars = cvx.Variable(right.shape[0])

    constraints = []

    for coefs, scalar in zip(right, left):

        x = vars[0] * coefs[0]
        for var, coef in zip(vars[1:], coefs[1:]): x += var * coef

        constraints.append(x == scalar) 


    return cvx.Problem(cvx.Maximize(vars[0]), constraints)


def CVX_vs_NP(size: int, itr: int) -> Tuple[float]:

    '''
    compares preformance on solving linear equasions systems
    between cvxpy and numpy.linalg

    size: of the random matrixes
    itr: number of iterations

    >>> cvx, np = CVX_vs_NP(10, 20)
    >>> print(type(cvx), type(np))
    <class 'float'> <class 'float'>
    '''

    cvx_run_time = 0
    np_run_time = 0

    for n, (right, left) in zip(range(itr), GenRanLinSys(size)):

        prb = CVXbuild(right, left)
        start = perf_counter()
        prb.solve()
        cvx_run_time += perf_counter() - start

        start = perf_counter()
        np.linalg.solve(right, left)
        np_run_time += perf_counter() - start

    return cvx_run_time, np_run_time
        

'''Correctness Test'''

for n, (right, left) in zip(range(10), GenRanLinSys(3)):

    prb = CVXbuild(right, left)

    assert round(np.linalg.solve(right, left)[0]) == round(prb.solve())


if __name__ == '__main__':
    
    print(*CVX_vs_NP(10, 20))

    doctest.testmod(verbose = True)