# So here we are trying to reshape the array into 3*3 array format
import numpy

somelist = input().split()
somelist = numpy.array(somelist).astype(int)
print(numpy.reshape(somelist,(3,3)))

"""
  INPUT
1 2 3 4 5 6 7 8 9
  OUTPUT
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
