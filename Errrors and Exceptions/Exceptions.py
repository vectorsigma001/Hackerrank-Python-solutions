T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)



"""
input
3
1 0
2 $
3 1

output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3


"""
