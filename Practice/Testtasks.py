import numpy as np
x = np.random.randint(1,10,size=(4,9))
print(x)


def slow(x):
    """Task"""
    d1, d2 = x.shape
    r = np.empty((d2, d1))
    for i in range(d1):
        for j in range(d2):
            r[j, i] = (i != j) * x[i, j] ** 2
    return r


def fast_mine(x):

    index_equal = np.zeros((x.shape))+np.arange(0,x.shape[-1]) != np.zeros((x.shape))+np.arange(0,x.shape[-2])[:,None]
    return index_equal.T * x.T**2

print(fast_mine(x))

print(slow(x))

print(f"\nTESTING: \n {slow(x)-fast_mine(x)}")