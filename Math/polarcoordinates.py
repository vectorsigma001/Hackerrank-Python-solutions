import cmath
def check(complexnumber):
    phase = cmath.phase(complexnumber)
    modulus_r = abs(complexnumber)
    return f"{modulus_r}\n{phase}"

if __name__ == "__main__":
    z = input()
    complexnumber = complex(z)
    print(check(complexnumber))

"""
      INPUT
1+2j
      OUTPUT
2.23606797749979
1.1071487177940904

"""
