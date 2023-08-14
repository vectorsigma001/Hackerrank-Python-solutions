"""
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i**2
Sample input  5
Sample output  0
               1
               4
               9
              16
"""
if __name__ == '__main__':
    n = int(input())
    i=0
    while(i<n):
        print(i**2)
        i=i+1
        
      
