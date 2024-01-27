# Here we are transposing and flattening an array
import numpy

n , m = map(int,input().split())
items = [list(map(int,input().split())) for m in range(n)]
reshapedarray = numpy.transpose(items)
flatteredarray = numpy.array(items).flatten()
print(reshapedarray)
print(flatteredarray)
