if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_score=student_marks.keys()
    for i in student_marks.keys():
        if query_name==i:
            SUM = sum(student_marks[i])
            avg = SUM/3
            print(f"{avg:.2f}")
