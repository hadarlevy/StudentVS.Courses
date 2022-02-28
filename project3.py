from functools import reduce


class Course:
    def __init__(self, name):
        self.course_name = name
        self.grade = 101

    def setGrade(self, grade1):
        if 100 >= grade1 >= 0:
            self.grade = grade1


class Student:
    def __init__(self, name, identity):
        self.courses_list = []
        self.student_name = name
        self.student_id = identity

    def getID(self):
        return self.student_id

    def addCourse(self, a_course):
        if 100 >= a_course.grade >= 0:
            self.courses_list.append(a_course)
            return
        assert a_course.grade > 100 or a_course.grade < 0, ""

    def average(self):
        arr = dict(map(lambda c: (c.course_name, c.grade), self.courses_list)).values()
        sum1 = sum(x for x in arr) / len(arr)
        return sum1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    f = input("press name of input-file !with txt ending!: ")
    try:
        file1 = open(f)
    except FileNotFoundError:
        print("not existed file")
        exit(1)
    student_list = []
    with open(f, 'r') as file1:
        for line in file1:
            student_name = line.split('\t')[0]
            student_id = line.split('\t')[1]
            student = Student(student_name, student_id)
            course_arr = line.split('\t')[2].replace('\n', "").split(';')
            for i in range(0, len(course_arr)):
                course_name = course_arr[i].split("#")[0]
                grade = int(course_arr[i].split("#")[1])
                course1 = Course(course_name)
                course1.setGrade(grade)
                student.addCourse(course1)
                student.courses_list = list({course1.course_name: course1 for course1 in student.courses_list}.values())
            student_list.append(student)
    choice = int(input("press your choice as:""\n""1-Calculating the average of a particular student.""\n""2-Calculating the average in a particular course.""\n""3-Average of all students.""\n""4-EXIT""\n"))
    while choice != 4:
        if choice == 1:
            name = input("press *exactly* the name of the student""\n")
            list1 = [s for s in student_list if s.student_name == name]
            if len(list1) == 0:
                print("ERROR, student does not exist")
            else:
                print(list1[0].student_id)
                print(list1[0].average())
        if choice == 2:
            arr = []
            name = input("press *exactly* the name of the course""\n")
            arr = list(filter(lambda x: x > -1, map(lambda s: dict(map(lambda c: (c.course_name, c.grade), s.courses_list)).get(name, -1), student_list)))
            print(sum(arr)/len(arr))
        if choice == 3:
            f2 = input("press name of output-file !with txt ending!: ")
            while True:
                if f == f2:
                    print("not valid file!, Pay Attention! this file is the input file from above")
                    break
                try:
                    file2 = open(f2)
                except FileNotFoundError:
                    print("not existed file")
                    break
                with open(f2, 'w') as file2:
                    list2 = [s for s in student_list]
                    list3 = [str(x. average()) + " " + x.student_id for x in list2]
                    final = "\n".join(list3)
                    file2.write(final)
                break
        if choice == 4:
            exit(1)
        choice = int(input("press your choice as:""\n""1-Calculating the average of a particular student.""\n""2-Calculating the average in a particular course.""\n""3-Average of all students.""\n""4-EXIT""\n"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
