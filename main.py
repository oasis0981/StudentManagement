# -*- coding: utf-8 -*-
"""new_ver.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s5wna3G3AxFtjmNu3eCD3b7aTV8uixjK
"""

STR_FORMAT = '%8s%15s%10s%10s%10s%10s'

class Score:  # 학생 점수 정보를 세팅하는 클래스
  def __init__(self, info):
    self.id = info[0] 
    self.name = info[1]
    self.mid = info[2]
    self.final = info[3]
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

  def set_score(self, type, new_score):
    if type == "mid":
      self.mid = new_score
    elif type == "final":
      self.final = new_score
    self.calculate_average()
            
            
class StudentManager:   # 성적관리기능을 수행하는 클래스
  def __init__(self):
    self.stu_data = []
    self.read_from_file()
      
  def read_from_file(self):
    f = open("students.txt")
    lines = f.readlines()
    lines = list(map(lambda s: s.strip(), lines))
    f.close
    for line in lines:
      splitted = line.split("\t")
      self.stu_data.append(Score(splitted))
  
  def search(self, target, byID):
    result = []
    if byID == True:
      for i in range(len(self.stu_data)):
        if self.stu_data[i].id == target:
          result.append(i)
    else:
      for i in range(len(self.stu_data)):
        if self.stu_data[i].grade == target:
          result.append(i)
    return result

  def avg_arr(self):
    self.stu_data.sort(reverse=True, key=lambda x: x.average)
      
  def print_data(self, print_format, indexes):
    if print_format == True:
      str_out = STR_FORMAT % ("Student", "Name", "Midterm", "Final", "Average", "Grade")
      print(str_out)
      print("-" * 70)
    for i in indexes:
      stu_data_out = STR_FORMAT % (self.stu_data[i].id, self.stu_data[i].name, self.stu_data[i].mid, self.stu_data[i].final, self.stu_data[i].average, self.stu_data[i].grade)
      print(stu_data_out)

  def change_score(self, index, test_type, score):
    for i in index:
      self.stu_data[i].set_score(test_type, score)

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
        if not self.stu_data:
          print("List is empty.")       
        self.run_remove()
      if a.upper() == 'QUIT':
        save_or_not = input("Save data?[yes/no] ")
        if save_or_not.upper() == "YES":
            self.save_data()
        break
      print("") # 명령 실행 후 한 줄 공백
              
  def run_show(self):
    self.avg_arr()
    self.print_data(True, list(range(len(self.stu_data))))
  
  def run_search(self):
    stu_id = input("Student ID: ")
    result = self.search(stu_id, byID = True)
    if result == []:
      print("NO SUCH STUDENT.")
    else:
      self.print_data(True, result)
  
  def run_change_score(self):
    stu_id = input("Student ID: ")
    result = self.search(stu_id, byID = True)
    if result == []:
      print("NO SUCH PERSON.")
    else:
      test = input("mid/final? ")
      if test == "mid" or test == "final":
        new_score = int(input("Input new score: "))
        if 0 <= new_score <= 100:
          self.print_data(True, result)
          self.change_score(result, test, new_score)
          print("Score changed.")
          self.print_data(False, result)

  def run_add(self):
    new_id = input("Student ID: ")
    result = self.search(new_id, byID=True)
    if len(result) > 0:
      print('ALREADY EXISTS.')
    else:
      name = input("Name: ")
      mid = input("Midterm Score: ")
      fin = input("Final Score: ")
      new_stu = Score([new_id, name, mid, fin])
      if 0 <= int(new_stu.mid) <= 100 and 0 <= int(new_stu.final) <= 100:
        print("Student added.")
        self.stu_data.append(new_stu)
    
  def run_search_grade(self):
    grade_to_search = input("Grade to search: ")
    result = self.search(grade_to_search, byID=False)
    if grade_to_search == 'A' or grade_to_search == 'B' or grade_to_search == 'C' or grade_to_search == 'D' or grade_to_search == 'F':
      if len(result) > 0:
        self.print_data(True, result)
      else:
        print("NO RESULTS.")

  def run_remove(self):
    remove_id = input("Student ID: ")
    result = self.search(remove_id, byID=True)
    if len(result) > 0:
        for i in result:
            del self.stu_data[i]
        print("Student removed.")
    else:
        print("NO SUCH PERSON.")

  def save_data(self):
    self.avg_arr()
    filename = input("File name: ")
    with open(filename, 'w', encoding='UTF-8') as f:
      for i in range(len(self.stu_data)):
        self.stu_data[i].mid = str(self.stu_data[i].mid)
        self.stu_data[i].final = str(self.stu_data[i].final)
        stu = self.stu_data[i].id + '\t' + self.stu_data[i].name + '\t' + self.stu_data[i].mid + '\t' + self.stu_data[i].final
        f.write(stu + '\n')

## main ##
m = StudentManager()
m.run()