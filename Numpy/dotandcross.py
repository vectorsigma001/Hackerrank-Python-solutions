import numpy as np
N =int(input())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A = np.array(A)
for _ in range(N):
    B.append(list(map(int, input().split())))
B = np.array(B)
print(np.dot(A,B))

"""
input
2
1 2
3 4
1 2
3 4
output
[[ 7 10]
 [15 22]]

"""
