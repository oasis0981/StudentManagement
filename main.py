STR_FORMAT = '%8s%15s%10s%10s%10s%10s'

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

def print_format():
    str_out = STR_FORMAT % ("Student", "Name", "Midterm", "Final", "Average", "Grade")
    print(str_out)
    print("-" * 70)

def print_data(indexes):
    for i in indexes:
        stu_data_out = STR_FORMAT % (stuData[i][0], stuData[i][1], stuData[i][2], stuData[i][3], stuData[i][4], stuData[i][5])
        print(stu_data_out)

def avg_arr():
    stuData.sort(reverse=True, key=lambda x: x[4])

def search(target, by):
    result = []
    for i in range(len(stuData)):
        if stuData[i][by] == target:
            result.append(i)
    return result


def run_show():
    avg_arr()
    print_format()
    print_data(list(range(len(stuData))))

def run_search():
    studentID = input("Student ID: ")
    a = search(studentID, 0)
    if len(a) > 0:
        print_format()
        print_data(a)

    else:
        print("NO SUCH STUDENT.")

def run_change_score():
    def change_score(test_type, new_score):
        stuData[i][test_type] = new_score
        stuData[i][4] = (int(stuData[i][2]) + int(stuData[i][3])) / 2
        grade(stuData[i][4])

    def a_score_print(i):
        print_format()
        print_data(i)

    def change_score_input():
        studentID = input("Student ID: ")
        result = search(studentID, 0)
        if len(result) > 0:
            test_type_input = input("Mid/Final? ")
            if test_type_input == 'mid':
                return 2
            elif test_type_input == 'final':
                return 3
        else:
            print("NO SUCH PERSON.")

    test_type = change_score_input()
    if test_type == 2 or test_type == 3:
        new_score = input("Input new score: ")
        if 0 <= int(new_score) <= 100:
            a_score_print()
            change_score(test_type, new_score)
            print("Score changed.")
            print_data(i)

def run_add():
    new_student_id = input("Student ID: ")
    new_student_data = []

    def add_new_data_list(list):
        list.append(new_student_id)
        list.append(input("Name: "))
        list.append(input("Midterm Score: "))
        list.append(input("Final Score: "))
        list.append((int(list[2]) + int(list[3])) / 2)

    result = search(new_student_id, 0)
    if len(result) > 0:
        print('ALREADY EXISTS.')
    else:
        add_new_data_list(new_student_data)
        if 0 <= int(new_student_data[2]) <= 100 and 0 <= int(new_student_data[3]) <= 100:
            add_grade(new_student_data[4], new_student_data)
            print("Student added.")
            stuData.append(new_student_data)
        avg_arr()

def run_search_grade():
    grade_to_search = input("Grade to search: ")
    result = search(grade_to_search, 5)
    if len(result) > 0:
        print_format()
        print_data(result)
    else:
        print("NO RESULTS.")


def run_remove():
    removeID = input("Student ID: ")
    result = search(removeID, 0)
    if len(result) > 0:
        for i in result:
            del stuData[i]
        print("Student removed.")
    else:
        print("NO SUCH PERSON.")

def save_data():
    filename = input("File name: ")
    avg_arr()
    with open(filename, 'w', encoding='UTF-8') as f:
        for i in range(len(stuData)):
            f.write('\t'.join(map(str, stuData[i])) + '\n')


f = open("C:/StudentFile/Students.txt")
lines = f.readlines()
lines = list(map(lambda s: s.strip(), lines))
f.close

stuData = []
for i in range(len(lines)):
    stuData.append(lines[i].split("\t"))
    stuData[i].append((int(stuData[i][2]) + int(stuData[i][3])) / 2)
    add_grade(stuData[i][4], stuData[i])

while True:
    a = input("# ")

    if a.upper() == 'SHOW':
        run_show()

    if a.upper() == 'SEARCH':
        run_search()

    if a.upper() == 'CHANGESCORE':
        run_change_score()

    if a.upper() == 'ADD':
        run_add()

    if a.upper() == 'SEARCHGRADE':
        run_search_grade()

    if a.upper() == 'REMOVE':
        if not stuData:
            print("List is empty.")
            break
        run_remove()

    if a.upper() == 'QUIT':
        save_or_not = input("Save data?[yes/no] ")
        if save_or_not.upper() == "YES":
            save_data()
        break

# if __name__ == "__main__":
#     print('hello world')