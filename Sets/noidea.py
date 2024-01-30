"""
            SOLUTION
"""
def check_happiness(A, B, somearray):
    A = set(A)
    B = set(B)
    happiness = sum(1 for element in somearray if element in A) - sum(1 for element in somearray if element in B)
    return happiness
          
if __name__ == "__main__":
    n , m = map(int, input().split())
    somearray = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(check_happiness(A, B, somearray))

"""
      INPUT
3 2
1 5 3
3 1
5 7

OUTPUT
1
"""
"""
            THE PROBLEM CAN BE SOLVED BY BELOW WAY TOO BUT THIS IS A SET PROBLEM  
"""
def check_happiness(A, B, somearray):
    happiness = 0
    for i in range(len(A)):
        for j in range(len(somearray)):
            if A[i] == somearray[j]:
                happiness = happiness + 1
            elif B[i] == somearray[j]:
                happiness = happiness - 1
    return happiness
          
if __name__ == "__main__":
    n , m = map(int, input().split())
    somearray = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(check_happiness(A, B, somearray))
