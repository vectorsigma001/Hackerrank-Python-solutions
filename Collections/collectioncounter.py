from collections import Counter

# number of shoe size
X = int(input())

# all the shoe size 
shoe_size_list = list(map(int, input().split()))

# Count the available shoe sizes
shoe_inventory = Counter(shoe_size_list)

# number of customers
N = int(input())

total_earnings = 0

for _ in range(N):
    shoe_size, price = map(int, input().split())

    if shoe_inventory[shoe_size] > 0:
        # Add the price to the total earnings
        total_earnings += price
        shoe_inventory[shoe_size] -= 1
        
print(total_earnings)

"""
input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

output
200

"""
