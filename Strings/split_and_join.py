# split and join the below string 
def split_and_join(line):
    splittedstring = line.split(" ")
    joinedstring = "-".join(splittedstring)
    return joinedstring
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# input
# this is a string

# output
# this-is-astring
