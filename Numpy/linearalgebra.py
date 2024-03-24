import numpy as np

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(float, input().split())))
A = np.array(A)
print(round(np.linalg.det(A),2))

"""
input
2
1.1 1.1
1.1 1.1

output
0.0

"""
