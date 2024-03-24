import numpy as np
P = list(map(float, input().split()))
P = np.array(P)
x = int(input())
print(np.polyval(P,x))


"""
input 
1.1 2 3
0

output
3.0
"""
