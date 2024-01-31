from itertools import product
if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in (product(A,B)):
        print(i, end=' ')

"""
    INPUT
1 2
3 4

    OUTPUT
(1, 3) (1, 4) (2, 3) (2, 4)
"""
