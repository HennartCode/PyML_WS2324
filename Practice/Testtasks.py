import numpy as np
x = np.random.randint(0,10,size=(4,9))
#x = np.random.random((7,16))
#print(x)

#--------------------111
# def slow(x):
#     """Task"""
#     d1, d2 = x.shape
#     r = np.empty((d2, d1))
#     for i in range(d1):
#         for j in range(d2):
#             r[j, i] = (i != j) * x[i, j] ** 2
#     return r

# def fast(x):
#     idxs = np.nonzero(np.ones(x.shape))
#     idxs0 = idxs[0].reshape(x.shape).T
#     idxs1 = idxs[1].reshape(x.shape).T
#     mask = 1 - (idxs0 == idxs1)
#     return mask * x.T **2





# def fast_mine(x):

#     index_equal = np.zeros((x.shape))+np.arange(0,x.shape[-1]) != np.zeros((x.shape))+np.arange(0,x.shape[-2])[:,None]
#     return index_equal.T * x.T**2



#---------------------------2222


# def slow(x):
# #"""Task"""
#     count = 0
#     for i in range(len(x)):
#         a = x[i, 0]**2
#         b = x[i, 1] ** 2
#         c = x[i, 2] ** 2
#         if a + b + c <= 1:
#             count += 1
#     return count

# def fast(x):
#     three_cols_squrared_collapsed = np.sum(x[:,:3]**2,axis=-1)
#     boolsches_arr = three_cols_squrared_collapsed <= 1
#     return boolsches_arr.sum()

# def fast_mine(x):
#     print(x[:,:3] ** 2)
#     #return x[:,:3] ** 2
#     print(np.sum((x[:,:3] ** 2),axis=1))
#     return np.arange(x.shape[-2])[(np.sum((x[:,:3] ** 2),axis=-1) > 1)]
#     return np.arange(x.shape[-2])

#Versuch: quadriurung der ersten drei Säulen, dann Summierung entlang der Zeilen. Dann vergleich ob größer 1 => boolesches Array. Dann ersten True wert Finden => Indice ist lösung



#---------------------------3333



# def slow(x):
#         """Task"""
#         d1, d2 = x.shape
#         r = np.zeros((d2, d2))
#         for i in range(d2):
#             for j in range(d2):
#                 for k in range(d1):
#                     r[i, j] += np.abs(x[k, i] * x[k, j])
#         return r

# def fast(x):
#     #return np.outer(x[:,None],x[:,None]).shape

#     outers = x[:,:,None] * x[:,None]
#     return np.sum(outers,axis=-3)









# def fast_mine(x):
#     # m = np.zeros((x.shape[-2],x.shape[-1],x.shape[-1]))
#     #m += np.arange(x.shape[-2])[:,None,None]
#      #m = np.concatenate(x * x[m[],x.shape[-1]])
#      return x.T @ x
#      return np.sum(m,axis=-2)


#-----------------------------44(from lecture2)

# def slow(x):
#     d1, d2 = x.shape
#     assert np.all([i >= 2 for i in (d1, d2)])
#     r = np.zeros((2, d1))
#     for i in range(d1):
#         for j in range(d2):
#             for k in range(2):
#                 r[k, i] += (x[k, j] - x[i, j]) ** 2
#     return r


# def fast(x):

#     return np.sum((x[:2,None] - x)**2,axis=-1)




# def fast(x):
    
#     return np.sum((x[:2,None] - x)**2,axis=-1)







# def fast_mine(x):
#     return np.sum(((x[:2,None]-x)**2),axis=-1)

# def fast(x):
#     assert x.shape[0] >= 2
#     diff = x[None, :, :] - x[:, None, :]
#     squared_distances = np.sum(diff**2, axis=2)
#     return squared_distances














# print(slow(x))

# print(fast(x))

#print(f"\nTESTING: \n {slow(x)-fast_mine(x)}")





#searchsorted([3, 4, 8, 17, 42], 12) -> 2
#searchsorted([5, 9, 14, 18], 1000) -> 3
#searchsorted([7, 293], 5) -> -1
#searchsorted([], 2) -> -1

tests = {1:([3, 4, 8, 17, 42],12),2:([5, 9, 14, 18],1000),3:[7, 293],4:[]}

a = tests[1]


def searchsorted(a,y):
    b_a = np.asarray(a) < y
    if any(b_a):
        return np.max(np.nonzero(b_a))
    else:
        return -1


print(searchsorted([3, 4, 8, 17, 42], 12))