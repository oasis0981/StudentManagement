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
    StuData[i][1] = StuData[i][1] + ' ' + StuData[i][2]
    del StuData[i][2]


StuAvg = []
StuAvg = list(map(float,StuAvg))
for i in range(5):
    StuAvg.append((int(StuData[i][2]) + int(StuData[i][3])) / 2)
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

StuData.sort(reverse=True, key=lambda x:x[4])

strFormat = '%8s%15s%10s%10s%10s%10s'
strOut = strFormat % ("Student", "Name", "Midterm", "Final", "Average", "Grade")


a = input()
if a.upper() == 'SHOW':
    print(strOut)
    print("-" * 70)
    for i in range(5):
        StuDataOut = strFormat % (StuData[i][0],StuData[i][1],StuData[i][2],StuData[i][3],StuData[i][4],StuData[i][5])
        print(StuDataOut)


if a.upper() == 'SEARCH':
    StudentID = input("Student ID: ")
    for i in range(5):
        if StuData[i][0] == StudentID:
            print(strOut)
            print("-" * 70)
            StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
            print(StuDataOut)
        else:
            print('NO SUCH PERSON.')
            break