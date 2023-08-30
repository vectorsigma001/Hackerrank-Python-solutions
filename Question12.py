"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer  at position .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7.. reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where
each command will be of the  types listed above. Iterate through each command in
order and perform the corresponding operation on your list.

#okay
Sample Input
     12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

Sample Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
""
#not done anything by today


#SOLUTION
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        cmd = input().strip().split()

        if cmd[0] == "insert":
            i, e = int(cmd[1]), int(cmd[2])
            lst.insert(i, e)
        elif cmd[0] == "print":
            print(lst)
        elif cmd[0] == "remove":
            e = int(cmd[1])
            lst.remove(e)
        elif cmd[0] == "append":
            e = int(cmd[1])
            lst.append(e)
        elif cmd[0] == "sort":
            lst.sort()
        elif cmd[0] == "pop":
            lst.pop()
        elif cmd[0] == "reverse":
            lst.reverse()

