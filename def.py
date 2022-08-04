from main import StuData


def grade(avg):
    if avg >= 90:
        StuData[i][5] = 'A'
    elif avg >= 80:
        StuData[i][5] = 'B'
    elif avg >= 70:
        StuData[i][5] = 'C'
    elif avg >= 60:
        StuData[i][5] = 'D'
    else:
        StuData[i][5] = 'F'

def addgrade(avg,list):
    if avg >= 90:
        list.append('A')
    elif avg >= 80:
        list.append('B')
    elif avg >= 70:
        list.append('C')
    elif avg >= 60:
        list.append('D')
    else:
        list.append('F')

def printFormat():
    print(strOut)
    print("-" * 70)
def printData():
    StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
    print(StuDataOut)

def changescore(testType):
    newScore = input("Input new score: ")
    if 0 <= int(newScore) <= 100:
    printFormat()
    printData()
    StuData[i][testType] = newScore
    StuData[i][4] = (int(StuData[i][2]) + int(StuData[i][3])) / 2
    grade(StuData[i][4])
    print("Score changed.")
    printData()

def avgArr():
    StuData.sort(reverse=True, key=lambda x: x[4])

def show():
    avgArr()
    printFormat()
    for i in range(len(StuData)):
        printData()

def search():
    for i in range(len(StuData)):
        if StuData[i][0] == StudentID:
            printFormat()
            printData()
            break
    else:
        print("NO SUCH STUDENT.")