import numpy as np

N, M = map(int, input().split()) 
listcheck = []
for _ in range(N):
    listcheck.append(list(map(int, input().split())))
my_array = np.array(listcheck)
check = np.sum(my_array, axis=0)
print(np.product(check))

"""
input
2 2
1 2
3 4

output
24
"""
