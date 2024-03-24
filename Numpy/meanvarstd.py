import numpy as np
N, M = map(int, input().split())  
my_array = []
for _ in range(N):
    my_array.append(list(map(int, input().split())))  
my_array = np.array(my_array)
print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print(f'{np.std(my_array, axis=None):.11f}')

"""
input
2 2
1 2
3 4

output
[1.5 3.5]
[1. 1.]
1.11803398875

"""
