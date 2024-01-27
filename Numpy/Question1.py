import numpy
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = numpy.array(input().split(), float)
    b = numpy.array(input().split(), float)

    # here I am performing addition
    summation = numpy.add(a, b).astype(int)
    difference = numpy.subtract(a, b).astype(int)
    multiplication = numpy.multiply(a, b).astype(int)
    division = numpy.divide(a, b).astype(int)
    mod = numpy.mod(a, b).astype(int)
    power = numpy.power(a, b).astype(int)
    
    print(summation.reshape(1, -1))
    print(difference.reshape(1, -1))
    print(multiplication.reshape(1, -1))
    print(division.reshape(1, -1))
    print(mod.reshape(1, -1))
    print(power.reshape(1, -1))
