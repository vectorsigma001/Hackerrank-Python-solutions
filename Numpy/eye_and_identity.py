import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n,m))

"""
input
3 3
output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""
