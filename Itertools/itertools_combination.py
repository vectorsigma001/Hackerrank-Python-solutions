"""
THIS ONE IS NOT MY SOLUTION
"""
from itertools import combinations
a,n=input().split()
t=list(a)
t.sort()
k=0
for i in range(int(n)):
    li=list(combinations(t,i+1))
    for j in li:
        ans=''.join(j)
        print(ans)

"""
    INPUT
HACK 2
    OUTPUT
A
C
H
K
AC
AH
AK
CH
CK
HK
"""
