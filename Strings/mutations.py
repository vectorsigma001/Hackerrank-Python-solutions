# STRINGS ARE IMMUTABLE , HOW CAN YOU CHANGE THE STRINGS 
def mutate_string(string, position, character):
    newstring = string[:position] + character + string[position + 1:]
    return newstring
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

"""
  SAMPLE INPUT
abracadabra
5 k

  SAMPLE OUTPUT
abracadabra
"""
