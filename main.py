from enum import Enum

STR_FORMAT = '%8s%15s%10s%10s%10s%10s'

class Student:
    def __init__(self, info):
        self.id = info[0] #id는 필드
        self.name = info[1]
        self.mid = info[2]
        self.final = info[3]
        self.calculate_average()

    def set_score(self, type, new_score):
        if type == "mid":
            self.mid = new_score
        elif type == "final":
            self.final = new_score
        self.calculate_average()

    def calculate_average(self):
        self.average = (int(self.mid) + int(self.final)) / 2
        self.calculate_grade()

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

def change_score(index, test_type, score):
    for i in index:
        stuData[i].set_score(test_type, score)

def get_info(words):
    input_info = input(words)
    return input_info

def print_data(print_format, indexes):
    if print_format == True:
        str_out = STR_FORMAT % ("Student", "Name", "Midterm", "Final", "Average", "Grade")
        print(str_out)
        print("-" * 70)
    for i in indexes:
        stu_data_out = STR_FORMAT % (stuData[i].id, stuData[i].name, stuData[i].mid, stuData[i].final, stuData[i].average, stuData[i].grade)
        print(stu_data_out)

def avg_arr():
    stuData.sort(reverse=True, key=lambda x: x.average)

def search(target, byID):
    return list(filter(lambda x: (stuData[x].id if byID else stuData[x].grade) == target, range(len(stuData))))

def run_show():
    avg_arr()
    print_data(True, list(range(len(stuData))))

def run_search():
    student_id = get_info("Student ID: ")
    result = search(student_id, byID=True)
    if len(a) > 0:
        print_data(print_format=True, indexes=result) #나중에 순서 바꿔서 고치기
    else:
        print("NO SUCH STUDENT.")

def run_change_score():
    student_id = get_info("Student ID: ")
    result = search(student_id, byID=True)
    if len(result) > 0:
        test_type = get_info("mid/final? ")
        if test_type == "mid" or test_type == "final":
            new_score = get_info("Input new score: ")
            if 0 <= int(new_score) <= 100:
                print_data(True, result)
                change_score(result, test_type, new_score)
                print("Score changed.")
                print_data(False, result)
    else:
        print("NO SUCH PERSON.")


def run_add():
    new_student_id = get_info("Student ID: ")
    result = search(new_student_id, byID=True)
    if len(result) > 0:
        print('ALREADY EXISTS.')
    else:
        new_student = Student([new_student_id, get_info("Name: "), get_info("Midterm Score: "), get_info("Final Score: ")])
        if 0 <= int(new_student.mid) <= 100 and 0 <= int(new_student.final) <= 100:
            print("Student added.")
            stuData.append(new_student)
            avg_arr()

def run_search_grade():
    grade_to_search = input("Grade to search: ")
    result = search(grade_to_search, byID=False)
    if len(result) > 0:
        print_data(True, result)
    else:
        print("NO RESULTS.")


def run_remove():
    removeID = input("Student ID: ")
    result = search(removeID, byID=True)
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
for line in lines:
    splitted = line.split("\t")
    stuData.append(Student(splitted))



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