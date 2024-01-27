"""
You are given two integer array a and b
and perform differet operations

"""
import numpy

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = numpy.array(input().split(), float)
        a.append(row)
    a = numpy.array(a)
    
    b = []
    for _ in range(n):
        row = numpy.array(input().split(), float)
        b.append(row)
    b = numpy.array(b)

    summation = numpy.add(a, b).astype(int)
    difference = numpy.subtract(a, b).astype(int)
    multiplication = numpy.multiply(a, b).astype(int)
    division = numpy.divide(a, b).astype(int)
    mod = numpy.mod(a, b).astype(int)
    power = numpy.power(a, b).astype(int)

    print(summation)
    print(difference)
    print(multiplication)
    print(division)
    print(mod)
    print(power)

"""
input
1 4
1 2 3 4
5 6 7 8
"""

"""
output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]

"""
