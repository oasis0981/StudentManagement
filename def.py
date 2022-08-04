strFormat = '%8s%15s%10s%10s%10s%10s'
strOut = strFormat % ("Student", "Name", "Midterm", "Final", "Average", "Grade")

stuData = []
for i in range(5):
    stuData.append(lines[i].split())
    stuData[i][1] = stuData[i][1] + ' ' + stuData[i][2]
    del stuData[i][2]

stuAvg = []
stuAvg = list(map(float,stuAvg))
for i in range(5):
    stuAvg.append((int(stuData[i][2]) + int(stuData[i][3])) / 2)
    stuData[i].append(stuAvg[i])


def grade(avg):
    if avg >= 90:
        stuData[i][5] = 'A'
    elif avg >= 80:
        stuData[i][5] = 'B'
    elif avg >= 70:
        stuData[i][5] = 'C'
    elif avg >= 60:
        stuData[i][5] = 'D'
    else:
        stuData[i][5] = 'F'

def add_grade(avg,list):
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

stuGrade = []
for i in range(5):
    add_grade(stuAvg[i], stuGrade)
    stuData[i].append(stuGrade[i])

def print_format():
    print(strOut)
    print("-" * 70)
def print_data(i):
    stuDataOut = strFormat % (stuData[i][0], stuData[i][1], stuData[i][2], stuData[i][3], stuData[i][4], stuData[i][5])
    print(stuDataOut)
def avg_arr():
    stuData.sort(reverse=True, key=lambda x: x[4])


def show():
    avg_arr()
    print_format()
    for i in range(len(stuData)):
        print_data(i)


def change_score(testType):
    newScore = input("Input new score: ")
    if 0 <= int(newScore) <= 100:
        print_format()
        print_data(i)
        stuData[i][testType] = newScore
        stuData[i][4] = (int(stuData[i][2]) + int(stuData[i][3])) / 2
        grade(stuData[i][4])
        print("Score changed.")
        print_data(i)


def search():
    for i in range(len(stuData)):
        if stuData[i][0] == studentID:
            print_format()
            print_data(i)
            break
    else:
        print("NO SUCH STUDENT.")


def add():
    for i in range(len(stuData)):
        if stuData[i][0] == newStudentID:
            print('ALREADY EXISTS.')
            break
    else:
        newName = input("Name: ")
        newMidScore = input("Midterm Score: ")
        newFinalScore = input("Final Score: ")
        newStudent = [newStudentID, newName, newMidScore, newFinalScore]
        newStudent.append((int(newStudent[2]) + int(newStudent[3])) / 2)
        if 0 <= int(newMidScore) <= 100 and 0 <= int(newFinalScore) <= 100:
            add_grade(newStudent[4], newStudent)
            print("Student added.")
            stuData.append(newStudent)
        avg_arr()

def search_grade():
    grade = ['A', 'B', 'C', 'D', 'F']
    for i in range(len(stuData)):
        if stuData[i][5] == searchGrade:
            print_format()
            break
    for i in range(5):
        if grade[i] == searchGrade:
            for i in range(len(stuData)):
                if stuData[i][5] == searchGrade:
                    break
            else:
                print("NO RESULTS.")
            for i in range(len(stuData)):
                if stuData[i][5] == searchGrade:
                    print_data(i)
                    continue
                elif stuData[i][5] != searchGrade:
                    pass

def remove():
    removeID = input("Student ID: ")
    for i in range(len(stuData)):
        if stuData[i][0] == removeID:
            del stuData[i]
            print("Student removed.")
            break
    else:
        print("NO SUCH PERSON.")


def quit():
    filename = input("File name: ")
    avg_arr()
    with open(filename, 'w', encoding='UTF-8') as f:
        for i in range(len(stuData)):
            f.write('\t'.join(map(str, stuData[i])) + '\n')