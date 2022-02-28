from functools import reduce


class Course:
    def __init__(self, name):
        self.course_name = name
        self.grade = 101

    def setGrade(self, grade1):
        if 100 >= grade1 >= 0:
            """check if the grade is valid if isn't it stays as 101"""
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
            """check if the grade is valid if isn't the course won't be appended to the course list of the student"""
            self.courses_list.append(a_course)
            return
        assert a_course.grade > 100 or a_course.grade < 0, ""
        """in case of invalid grade acceptation will be called"""

    def average(self):
        """
        a function that calculate the average of current student
        :return: the average
        """
        arr = dict(map(lambda c: (c.course_name, c.grade), self.courses_list)).values()
        arr = arr
        """ arr= a list of the grades of each course by its name"""
        sum1 = sum(map(lambda x: x, arr)) / len(arr)
        return sum1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    f = input("press name of input-file !with txt ending!: ")
    """input the name of the file from the user"""
    try:
        file1 = open(f)
        """try to open this file by the name"""
    except FileNotFoundError:
        print("not existed file")
        exit(1)
        """if the file doesn't exist stop the program"""
    student_list = []
    with open(f, 'r') as file1:
        for line in file1:
            """for each line in the file do:"""
            student_name = line.split('\t')[0]
            """get the student name"""
            student_id = line.split('\t')[1]
            """get the student id"""
            student = Student(student_name, student_id)
            """build an object of student"""
            course_arr = line.split('\t')[2].replace('\n', "").split(';')
            """get the list of curses of this student in this line"""
            for i in range(0, len(course_arr)):
                """for each place in courses list do:"""
                course_name = course_arr[i].split("#")[0]
                """get the name of the course"""
                grade = int(course_arr[i].split("#")[1])
                """get the grade and convert it to int from str"""
                course1 = Course(course_name)
                """build an object of Course"""
                course1.setGrade(grade)
                """check if the grade is valid"""
                student.addCourse(course1)
                """add the course to the list"""
                student.courses_list = list({course1.course_name: course1 for course1 in student.courses_list}.values())
                """check if this specific course is already in the list and update to the last one in that case"""
            student_list.append(student)
            """add this student to the list of the students"""
    choice = int(input("press your choice as:""\n""1-Calculating the average of a particular student.""\n"""
                       "2-Calculating the average in a particular course.""\n""3-Average of all students.""\n""4-EXIT"""
                       "\n"))
    while choice != 4:
        if choice == 1:
            name = input("press *exactly* the name of the student""\n")
            list1 = list(filter(lambda s: s.student_name == name, student_list))
            # list1 = [s for s in student_list if s.student_name == name]
            """list1 = the student from the students list that his name is equal as the name that the use pressed"""
            if len(list1) == 0:
                """if list1 is empty it means that there isn't student with this name"""
                print("ERROR, student does not exist")
            else:
                print(list1[0].student_id)
                print(list1[0].average())
        if choice == 2:
            arr = []
            name = input("press *exactly* the name of the course""\n")
            arr = list(filter(lambda x: x > -1, map(lambda s: dict(map(lambda c: (c.course_name, c.grade), s.courses_list)).get(name, -1), student_list)))
            """arr = list of the grades of the course with the name that the user pressed of all the student"""
            """we assumed that the name is valid cause we didn't asked to check it"""
            print(sum(arr)/len(arr))
            """the average..."""
        if choice == 3:
            f2 = input("press name of output-file !with txt ending!: ")
            while True:
                if f == f2:
                    """if the name of the file is the same name as the output file from above"""
                    print("not valid file!, Pay Attention! this file is the input file from above")
                    break
                try:
                    file2 = open(f2)
                    """try to open this file by the name"""
                except FileNotFoundError:
                    print("not existed file")
                    break
                    """if the file doesn't exist break"""
                with open(f2, 'w') as file2:
                    list2 = list(map(lambda s: s, student_list))
                    # list2 = [s for s in student_list]
                    """list2 = list of the students in the student list"""
                    list3 = list(map(lambda x: str(x.average()) + " " + x.student_id, list2))
                    # list3 = [str(x. average()) + " " + x.__student_id for x in list2]
                    """list3 = list of strings of average space and id of each student from list2"""
                    final = "\n".join(list3)
                    """ add a linebreak to each element in list3"""
                    file2.write(final)
                    """write to the file"""
                break
        if choice == 4:
            exit(1)
        choice = int(input("press your choice as:""\n""1-Calculating the average of a particular student.""\n""2-Calculating the average in a particular course.""\n""3-Average of all students.""\n""4-EXIT""\n"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
