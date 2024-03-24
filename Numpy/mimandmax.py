import numpy as np
N, M = map(int, input().split())  
listcheck = []
for _ in range(N):
    listcheck.append(list(map(int, input().split())))
my_array = np.array(listcheck)  
minimumvalue = np.min(my_array, axis=1)  
minimumindices= np.argmin(my_array, axis=1)  
maximumofminimum= np.max(minimumvalue)
print(maximumofminimum)

"""
input
4 2
2 5
3 7
1 3
4 0

output
3
"""
