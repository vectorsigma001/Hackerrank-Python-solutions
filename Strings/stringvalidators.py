if __name__ == '__main__':
    s = input()
    print(any(n.isalnum() for n in s))
    print(any(n.isalpha() for n in s))
    print(any(n.isdigit() for n in s))
    print(any(n.islower() for n in s))
    print(any(n.isupper() for n in s))


"""

input
qA2

output
True
True
True
True
True
"""
