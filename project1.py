f = open("C:/StudentFile/Students.txt")
lines = f.readlines()
f.close


# keys = []
# for i in range(5):
#    keys.append(lines[i][0:8])
# print(keys)

StuData = []
for i in range(5):
    StuData.append(lines[i].split())

StuAvg = []
StuAvg = list(map(float,StuAvg))
for i in range(5):
    StuAvg.append((int(StuData[i][3]) + int(StuData[i][4])) / 2)
    StuData[i].append(StuAvg[i])


StuGrade = []
for i in range(5):
    if StuAvg[i] >= 90:
        StuGrade.append('A')
    elif StuAvg[i] >= 80:
        StuGrade.append('B')
    elif StuAvg[i] >= 70:
        StuGrade.append('C')
    elif StuAvg[i] >= 60:
        StuGrade.append('D')
    else:
        StuGrade.append('F')
    StuData[i].append(StuGrade[i])


StuData.sort(reverse=True, key=lambda x:x[5])
# print(StuData)


a = input()
item = "Student Name Midterm Final Average Grade"
item.replace(" ", "\t")


if a.upper() == 'SHOW':
    print(item)
    print("-" * 50)
    for i in range(5):
        print('\t'.join(map(str, StuData[i])))
