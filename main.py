f = open("C:/StudentFile/Students.txt")
lines = f.readlines()
f.close


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



strFormat = '%8s%15s%10s%10s%10s%10s'
strOut = strFormat % ("Student", "Name", "Midterm", "Final", "Average", "Grade")

while True:
    a = input()
    if a.upper() == 'SHOW':
        StuData.sort(reverse=True, key=lambda x: x[4])
        print(strOut)
        print("-" * 70)
        for i in range(len(StuData)):
            StuDataOut = strFormat % (StuData[i][0],StuData[i][1],StuData[i][2],StuData[i][3],StuData[i][4],StuData[i][5])
            print(StuDataOut)


    if a.upper() == 'SEARCH':
        StudentID = input("Student ID: ")
        for i in range(len(StuData)):
            if StuData[i][0] == StudentID:
                print(strOut)
                print("-" * 70)
                StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
                print(StuDataOut)
                break
        else:
            print("NO SUCH STUDENT.")



    if a.upper() == 'CHANGESCORE':
        StudentID = input("Student ID: ")
        for i in range(len(StuData)):
            if StuData[i][0] == StudentID:
                testType = input("Mid/Final? ")
                if testType == 'mid':
                    newScore = input("Input new score: ")
                    if 0 <= int(newScore) <=100:
                        print(strOut)
                        print("-" * 70)
                        StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
                        print(StuDataOut)
                        StuData[i][2] = newScore
                        StuData[i][4] = (int(StuData[i][2]) + int(StuData[i][3])) / 2
                        if StuData[i][4] >= 90:
                            StuData[i][5] = 'A'
                        elif StuData[i][4] >= 80:
                            StuData[i][5] = 'B'
                        elif StuData[i][4] >= 70:
                            StuData[i][5] = 'C'
                        elif StuData[i][4] >= 60:
                            StuData[i][5] = 'D'
                        else:
                            StuData[i][5] = 'F'
                        print("Score changed.")
                        StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
                        print(StuDataOut)
                elif testType == 'final':
                    newScore = input("Input new score: ")
                    if 0 <= int(newScore) <=100:
                        print(strOut)
                        print("-" * 70)
                        StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
                        print(StuDataOut)
                        StuData[i][3] = newScore
                        StuData[i][4] = (int(StuData[i][2]) + int(StuData[i][3])) / 2
                        if StuData[i][4] >= 90:
                            StuData[i][5] = 'A'
                        elif StuData[i][4] >= 80:
                            StuData[i][5] = 'B'
                        elif StuData[i][4] >= 70:
                            StuData[i][5] = 'C'
                        elif StuData[i][4] >= 60:
                            StuData[i][5] = 'D'
                        else:
                            StuData[i][5] = 'F'
                        print("Score changed.")
                        StuDataOut = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
                        print(StuDataOut)
                StuData.sort(reverse=True, key=lambda x: x[4])
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
                if NewStudent[4] >= 90:
                    NewStudent.append('A')
                elif NewStudent[4] >= 80:
                    NewStudent.append('B')
                elif NewStudent[4] >= 70:
                    NewStudent.append('C')
                elif NewStudent[4] >= 60:
                    NewStudent.append('D')
                else:
                    NewStudent.append('F')
                print("Student added.")
                StuData.append(NewStudent)
            StuData.sort(reverse=True, key=lambda x: x[4])

    if a.upper() == 'SEARCHGRADE':
        grade = ['A', 'B', 'C', 'D', 'F']
        searchGrade = input("Grade to search: ")
        for i in range(len(StuData)):
            if StuData[i][5] == searchGrade:
                print(strOut)
                print("-" * 70)
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
                        StuSearchData = strFormat % (StuData[i][0], StuData[i][1], StuData[i][2], StuData[i][3], StuData[i][4], StuData[i][5])
                        print(StuSearchData)
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
        if saveornot == "yes":
            filename = input("File name: ")
            StuData.sort(reverse=True, key=lambda x: x[4])
            with open(filename,'w',encoding='UTF-8') as f:
                for i in range(len(StuData)):
                    f.write('\t'.join(map(str,StuData[i]))+'\n')
        break