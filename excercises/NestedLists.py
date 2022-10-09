if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    lowestGrade=min(records, key = lambda x: x[1])[1]
    records = [student for student in records if student[1]!=lowestGrade]
    if(records):
        lowestGrade = min(records, key = lambda x: x[1])[1]
        records = [student for student in records if student[1] == lowestGrade]
        records = sorted(records, key = lambda x: x[0])
    for s in records:
        print(s[0])
