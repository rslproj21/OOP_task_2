class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Имя: {self.name} \n Фамилия: {self.surname} \n' \
                       f'Средняя оценка за домашнее задание: {self.__calc_grades()} \n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)} \n' \
                       f'Завершенные курсы: {" ".join(self.finished_courses)}'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return best_student.__calc_grades() > second_student.__calc_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name} \n Фамилия: {self.surname}' \
                             f'{self.__calc_grades()}'
        return self.some_lecturer

    def __calc_grades(self):
        avg_score_py = sum(self.course_grades['PYTHON']) / len(self.course_grades['PYTHON'])
        avg_score_java = sum(self.course_grades['JAVA']) / len(self.course_grades['JAVA'])
        avg_score_py_and_java = (avg_score_py + avg_score_java) / len(self.course_grades)
        return round(avg_score_py_and_java, 1)

    def __lt__(self,other):
        if not isinstance(other, Lecturer):
            print('Не лектору')
            return
        return cool_lecturer.__calc_grades() < second_lecturer.__calc_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviewer = f'Имя: {self.name} \n Фамилия: {self.surname} \n'
        return self.some_reviewer

best_student = Student('Ruoy', 'Eman', 'Male')
best_student.courses_in_progress += ['PYTHON', 'JAVA']
best_student.finished_courses += ['Files']

second_student = Student('Ivan', 'Petrov', 'Male')
second_student.courses_in_progress += ['PYTHON', 'JAVA']
second_student.finished_courses += ['Files']

cool_lecturer = Mentor('Oleg', 'Ivanov')
cool_lecturer.courses_attached += ['PYTHON', 'JAVA']

second_lecturer = Lecturer('Nikita', 'Mikhailov')
second_lecturer.courses_attached += ['PYTHON', 'JAVA']

some_reviewer = Reviewer('Sam', 'Jackson')
some_reviewer.courses_attached += ['PYTHON', 'JAVA']

second_reviewer = Reviewer('Sergey', 'Ionov')
second_reviewer.courses_attached += ['PYTHON', 'JAVA']

best_student.rate_lecturer(cool_lecturer, 'PYTHON', 9)
best_student.rate_lecturer(cool_lecturer, 'PYTHON', 7)

best_student.rate_lecturer(cool_lecturer, 'JAVA', 8)
best_student.rate_lecturer(cool_lecturer, 'JAVA', 7)

second_student.rate_lecturer(second_lecturer, 'PYHTON', 7)
second_student.rate_lecturer(second_lecturer, 'PYTHON', 6)

second_student.rate_lecturer(second_lecturer, 'JAVA', 7)
second_student.rate_lecturer(second_lecturer, 'JAVA', 6)

some_reviewer.rate_hw(best_student, 'PYTHON', 10)
some_reviewer.rate_hw(best_student, 'PYTHON', 8)

some_reviewer.rate_hw(best_student, 'JAVA', 9)
some_reviewer.rate_hw(best_student, 'JAVA', 6)

some_reviewer.rate_hw(second_student, 'PYTHON', 8)
some_reviewer.rate_hw(second_student, 'PYTHON', 7)

some_reviewer.rate_hw(second_student, 'JAVA', 7)
some_reviewer.rate_hw(second_student, 'JAVA', 6)

students = [best_student, second_student]
all_lecturers = [cool_lecturer, second_lecturer]

def calc_avg_grades(student, course):
    grade_list = []
    for student in students:
        if course in student.grades:
            grade_list += student.grades[course]
        else:
            return 'Ошибка'
        grades_score = sum(grade_list) / len(grade_list)
    return round(grades_score, 1)

def calc_avg(lecturer, course):
    grade_list = []
    for lecturer in all_lecturers:
        if course in lecturer.course_grades:
            grade_list += lecturer.course_grades[course]
        else:
            return 'Ошибка'
        result = sum(grade_list) / len(grade_list)
    return round(result, 1)

print(f'Student: {best_student.__str__()}')
print(f'Student: {second_student.__str__()}')
print(f'Lecturer: {cool_lecturer.__str__()}')
print(f'Lecturer: {second_lecturer.__str__()}')
print(f'Reviewer: {some_reviewer.__str__()}')
print(f'Reviewer: {second_reviewer.__str__()}')

print('')

print(f'Средняя оценка у студента Ruoy Eman больше, чем у Ivan Petrov?: {best_student.__lt__(second_student)}')
print(f'Средняя оценка у лектора Oleg Ivanov меньше, чем у Nikita Mikhailov?: {cool_lecturer.__lt__(second_lecturer)}')
print(f'Средний балл у студентов по PYTHON: {calc_avg_grades(students, "PYTHON")}')
print(f'Средний балл у студентов по JAVA: {calc_avg_grades(students, "JAVA")}')

print('')

print(f'Средний балл среди лекторов по PYTHON: {calc_avg(all_lecturers, "PYTHON")}')
print(f'Средний балл среди лекторов по JAVA: {calc_avg(all_lecturers, "JAVA")}')

