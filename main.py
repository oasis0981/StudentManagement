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

class StudentManager:
    def __init__(self):
        self.stuData = []
        self.read_from_file()

    def read_from_file(self):
        f = open("C:/StudentFile/Students.txt")
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        f.close
        for line in lines:
            splitted = line.split("\t")
            self.stuData.append(Student(splitted))

    def run(self):
        while True:
            a = input("# ")

            if a.upper() == 'SHOW':
                self.run_show()

            if a.upper() == 'SEARCH':
                self.run_search()

            if a.upper() == 'CHANGESCORE':
                self.run_change_score()

            if a.upper() == 'ADD':
                self.run_add()

            if a.upper() == 'SEARCHGRADE':
                self.run_search_grade()

            if a.upper() == 'REMOVE':
                if not self.stuData:
                    print("List is empty.")
                    break
                self.run_remove()

            if a.upper() == 'QUIT':
                save_or_not = input("Save data?[yes/no] ")
                if save_or_not.upper() == "YES":
                    self.save_data()
                break

    def change_score(self, index, test_type, score):
        for i in index:
            self.stuData[i].set_score(test_type, score)

    def get_info(self, words):
        input_info = input(words)
        return input_info

    def print_data(self, print_format, indexes):
        if print_format == True:
            str_out = STR_FORMAT % ("Student", "Name", "Midterm", "Final", "Average", "Grade")
            print(str_out)
            print("-" * 70)
        for i in indexes:
            stu_data_out = STR_FORMAT % (self.stuData[i].id, self.stuData[i].name, self.stuData[i].mid, self.stuData[i].final, self.stuData[i].average, self.stuData[i].grade)
            print(stu_data_out)

    def avg_arr(self):
        self.stuData.sort(reverse=True, key=lambda x: x.average)

    def search(self, target, byID):
        return list(filter(lambda x: self.stuData[x].id if byID else self.stuData[x].grade == target, range(len(self.stuData))))

    def run_show(self):
        self.avg_arr()
        self.print_data(True, list(range(len(self.stuData))))

    def run_search(self):
        student_id = self.get_info("Student ID: ")
        result = self.search(student_id, byID=True)
        if len(result) > 0:
            self.print_data(print_format=True, indexes=result) #나중에 순서 바꿔서 고치기
        else:
            print("NO SUCH STUDENT.")

    def run_change_score(self):
        student_id = self.get_info("Student ID: ")
        result = self.search(student_id, byID=True)
        if len(result) > 0:
            test_type = self.get_info("mid/final? ")
            if test_type == "mid" or test_type == "final":
                new_score = self.get_info("Input new score: ")
                if 0 <= int(new_score) <= 100:
                    self.print_data(True, result)
                    self.change_score(result, test_type, new_score)
                    print("Score changed.")
                    self.print_data(False, result)
        else:
            print("NO SUCH PERSON.")


    def run_add(self):
        new_student_id = self.get_info("Student ID: ")
        result = self.search(new_student_id, byID=True)
        if len(result) > 0:
            print('ALREADY EXISTS.')
        else:
            new_student = Student([new_student_id, self.get_info("Name: "), self.get_info("Midterm Score: "), self.get_info("Final Score: ")])
            if 0 <= int(new_student.mid) <= 100 and 0 <= int(new_student.final) <= 100:
                print("Student added.")
                self.stuData.append(new_student)
                self.avg_arr()

    def run_search_grade(self):
        grade_to_search = input("Grade to search: ")
        result = self.search(grade_to_search, byID=False)
        if len(result) > 0:
            self.print_data(True, result)
        else:
            print("NO RESULTS.")


    def run_remove(self):
        removeID = input("Student ID: ")
        result = self.search(removeID, byID=True)
        if len(result) > 0:
            for i in result:
                del self.stuData[i]
            print("Student removed.")
        else:
            print("NO SUCH PERSON.")

    def save_data(self):
        filename = input("File name: ")
        self.avg_arr()
        with open(filename, 'w', encoding='UTF-8') as f:
            for i in range(len(self.stuData)):
                f.write('\t'.join(map(str, self.stuData[i])) + '\n')


manager = StudentManager()
manager.run()

# if __name__ == "__main__":
#     print('hello world')