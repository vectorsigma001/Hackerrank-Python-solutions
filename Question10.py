"""
Here you have given number of student names and score
print the second lowest student score 
print the score with names 
if the score is same print the score with name alphabetically 
"""
if __name__ == '__main__':
    li=[]
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record=[name,score]
        records.append(record)
    scores=[]
    #here we have sorted marks
    uniquescores=[]
    for records1 in records:
        scores.append(records1[1])
    #making the scores unique by using sets
    uniquescores=list(set(scores))
    
    uniquescores.sort()
    secondlowestscore=uniquescores[1]
    
    # Fetching names with the second lowest scores
    second_lowest_students = []
    for record in records:
        if record[1] == secondlowestscore:
            second_lowest_students.append(record[0])
    
    # Sorting the names alphabetically and printing them
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)
