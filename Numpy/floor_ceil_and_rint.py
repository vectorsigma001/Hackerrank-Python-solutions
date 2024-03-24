import numpy as np
np.set_printoptions(legacy='1.13')
my_array = np.array(input().split(), dtype=float)
print(np.floor(my_array))
print(np.ceil(my_array))
print(np.rint(my_array))

"""
input
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

output
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""
