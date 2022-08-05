
def score_input_and_change():
    def change_score(test_type):
        new_score = input("Input new score: ")
        if 0 <= int(new_score) <= 100:
            stuData[i][test_type] = new_score
            stuData[i][4] = (int(stuData[i][2]) + int(stuData[i][3])) / 2
            grade(stuData[i][4])
            print("Score changed.")
            print_format()
            print_data(i)
    for i in range(len(stuData)):
        if stuData[i][0] == studentID:
            test_type = input("Mid/Final? ")
            if test_type == 'mid':
                change_score(2)
            elif test_type == 'final':
                change_score(3)
            avg_arr()
            return True
