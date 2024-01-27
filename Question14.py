# Solutions yet to come
import numpy
n, m = map(int, input().split())
a = numpy.array(input().split(), float)
b = numpy.array(input().split(), float)

# here I am performing addition
summation = numpy.add(a, b)
for i in range(len(summation)):
    summation[i] = int(summation[i])
difference = numpy.subtract(a, b)
for i in range(len(difference)):
    difference[i] = int(difference[i])
multiplication = numpy.multiply(a, b)
for i in range(len(multiplication)):
    multiplication[i] = int(multiplication[i]) 
division = numpy.divide(a, b)
mod = numpy.mod(a, b)
power = numpy.power(a, b)

print(summation)
print(difference)
print(multiplication)
print(division)
print(mod)
print(power)
