import numpy as np
import numpy.random as rnd
import cvxpy as cvx



# distrabution

def GenRanLinSys() -> np.ndarray:
    '''
    random linear equations system
    random dimentions, random coefficients
    '''

    while True:

        # Last 2 dimensions of the array must be square (unique solution)
        dimentions = tuple(rnd.randint(1, 10, rnd.randint(1, 6))) + tuple([rnd.randint(1, 10)] * 2)

        yield rnd.uniform(-100, 100, dimentions), rnd.uniform(-100, 100, dimentions[:-1])


def CVX_vs_NP(left: np.ndarray, right: np.ndarray):

    arr = cvx.


if __name__ == '__main__':
    
    for n, (left,right ) in zip(range(10), GenRanLinSys()): print(np.linalg.solve(left, right))