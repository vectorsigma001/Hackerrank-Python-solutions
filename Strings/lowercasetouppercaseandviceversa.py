def swap_case(s):
    stringlist = list(s)
    if 0 < len(stringlist) <= 1000:
        for i in range(len(stringlist)):
            if ord(stringlist[i]) == ord(stringlist[i].upper()):
                stringlist[i] = str(stringlist[i]).lower()
            elif ord(stringlist[i]) == ord(stringlist[i].lower()):
                stringlist[i] = str(stringlist[i]).upper()            
    return ''.join(stringlist)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


"""
    INPUT
HackerRank.com presents "Pythonist 2".
    OUTPUT
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""
