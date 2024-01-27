"""
Take a number of items that needs to be in a tuple
Take a list of item in a single line
convert it into integer
convert it into tuple
and find the hash of it using hash() functions
"""
if __name__ == '__main__':
    numberofitems = int(input())
    valueinlist = input().split()
    for i in range(numberofitems):
        valueinlist[i] = int(valueinlist[i])
    # convert the list directly into integer
    # somelist = map(int,valueinlist)
    convertedtuple = tuple(valueinlist)
    result = hash(convertedtuple)
    print(result)
