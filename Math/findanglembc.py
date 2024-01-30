import math
def angle_mbc():
    side_ab = float(input())
    side_bc = float(input())
    hypotenuse = math.hypot(side_ab, side_bc) # FINDING HYPOTENUSE
    res=round(math.degrees(math.acos(side_bc/hypotenuse))) # FINDING THE ANGLE
    degree=chr(176)                                
    print(res,degree, sep='')
angle_mbc()

# tHIS IS NOT MY SOLUTION AT ALL
"""
    INPUT
10
10

    OUTPUT
45°
"""
