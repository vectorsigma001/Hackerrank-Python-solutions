# Here we have two list n and m
# we are concatenating n and m with axis 0
import numpy as np
N , M , P = map(int,input().split())
n = []
m = []
for _ in range(N):
    row = list(map(int, input().split()))
    n.append(row)
n = np.array(n)

for _ in range(M):
    row = list(map(int, input().split()))
    m.append(row)
m = np.array(m)

check = np.concatenate((n,m),axis=0)
print(check)
