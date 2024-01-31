from itertools import permutations    
if __name__ == '__main__':
    S , k = input().split()
    k = int(k)
    permutation = permutations(S, k)
    result = list(permutation)
    result.sort()
    for j in result:
        print(''.join(j))

"""
    INPUT
HACK 2

    OUTPUT
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""
