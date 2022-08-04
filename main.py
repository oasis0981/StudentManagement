f = open("C:/StudentFile/Students.txt")
lines = f.readlines()
f.close


strFormat = '%8s%15s%10s%10s%10s%10s'
strOut = strFormat % ("Student", "Name", "Midterm", "Final", "Average", "Grade")


def printFormat():
    print(strOut)
    print("-" * 70)
def printData():
    StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
    print(StuDataOut)
def avgArr():
    StuData.sort(reverse=True, key=lambda x: x[4])


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
    addgrade(StuAvg[i], StuGrade)
    StuData[i].append(StuGrade[i])


def show():
    avgArr()
    printFormat()
    for i in range(len(StuData)):
        printData()

def changeScore(testType):
    newScore = input("Input new score: ")
    if 0 <= int(newScore) <= 100:
        printFormat()
        printData()
        StuData[i][testType] = newScore
        StuData[i][4] = (int(StuData[i][2]) + int(StuData[i][3])) / 2
        grade(StuData[i][4])
        print("Score changed.")
        printData()


def search():
    for i in range(len(StuData)):
        if StuData[i][0] == StudentID:
            printFormat()
            printData()
            break
    else:
        print("NO SUCH STUDENT.")




while True:
    a = input()
    if a.upper() == 'SHOW':
        avgArr()
        printFormat()
        for i in range(len(StuData)):
            printData()
        show()

    if a.upper() == 'SEARCH':
        StudentID = input("Student ID: ")
        for i in range(len(StuData)):
            if StuData[i][0] == StudentID:
                printFormat()
                printData()
                break
        else:
            print("NO SUCH STUDENT.")



    if a.upper() == 'CHANGESCORE':
        StudentID = input("Student ID: ")
        for i in range(len(StuData)):
            if StuData[i][0] == StudentID:
                testType = input("Mid/Final? ")
                if testType == 'mid':
                    changeScore(2)
                elif testType == 'final':
                    changeScore(3)
                avgArr()
                break
        else:
            print('NO SUCH PERSON.')


    if a.upper() == 'ADD':
        NewStudentID = input("Student ID: ")
        for i in range(len(StuData)):
            if StuData[i][0] == NewStudentID:
                print('ALREADY EXISTS.')
                break
        else:
            NewName = input("Name: ")
            NewMidScore = input("Midterm Score: ")
            NewFinalScore = input("Final Score: ")
            NewStudent = [NewStudentID, NewName, NewMidScore, NewFinalScore]
            NewStudent.append((int(NewStudent[2]) + int(NewStudent[3])) / 2)
            if 0 <=int(NewMidScore) <= 100 and 0 <= int(NewFinalScore) <=100:
                addgrade(NewStudent[4],NewStudent)
                print("Student added.")
                StuData.append(NewStudent)
            avgArr()

    if a.upper() == 'SEARCHGRADE':
        grade = ['A', 'B', 'C', 'D', 'F']
        searchGrade = input("Grade to search: ")
        for i in range(len(StuData)):
            if StuData[i][5] == searchGrade:
                printFormat()
                break
        for i in range(5):
            if grade[i] == searchGrade:
                for i in range(len(StuData)):
                    if StuData[i][5] == searchGrade:
                        break
                else:
                    print("NO RESULTS.")
                for i in range(len(StuData)):
                    if StuData[i][5] == searchGrade:
                        printData()
                        continue
                    elif StuData[i][5] != searchGrade:
                        pass


    if a.upper() == 'REMOVE':
        if not StuData:
            print("List is empty.")
            break
        removeID = input("Student ID: ")
        for i in range(len(StuData)):
            if StuData[i][0] == removeID:
                del StuData[i]
                print("Student removed.")
                break
        else:
            print("NO SUCH PERSON.")


    if a.upper() == 'QUIT':
        saveornot = input("Save data?[yes/no] ")
        if saveornot.upper == "yes":
            filename = input("File name: ")
            StuData.sort(reverse=True, key=lambda x: x[4])
            with open(filename,'w',encoding='UTF-8') as f:
                for i in range(len(StuData)):
                    f.write('\t'.join(map(str,StuData[i]))+'\n')
        break