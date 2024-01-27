
import numpy

def arrays(arr):
    somearray = numpy.array(arr,float)
    changedarray = numpy.flip(somearray)
    somearray1 = numpy.array(changedarray)
    return somearray1
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

"""
    INPUT 
1 2 3 4 -8 -10

    OUTPUT
[-10.  -8.   4.   3.   2.   1.]
"""
