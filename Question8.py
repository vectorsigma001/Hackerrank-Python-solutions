"""
Here you have given x y and z , these represents the dimesion of the cuboid along with the integer n
In a 3D grid print all the coordinates which is given by i j and k 
where the sum of i j and k should not be greater than n
use list comprehension rather than multiple loops
""""
#Code

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    a.append([i,j,k])
    print(a)
    
