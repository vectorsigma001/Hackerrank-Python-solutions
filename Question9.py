""""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
my explanation
n means number of scores given 
in the arr the scores are stored of different participants
we are said to print the runner up student score
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    li=list(set(arr)) #first it is converted into set and then into list and the value is stored in li
    li.sort()
    r=li[-2]
    print(r)

"""
1.first the arr is converted into set 
2.then the set is converted into list and stored in li 
3. the list is sorted in ascending order
4. the runner up score is stored in r
5 . the runner up score been printed
"""
    
