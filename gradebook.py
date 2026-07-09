
class Gradebook:
    def __init__(self,passing_grade=55):
        self.students = []
        self.courses = []
        self.grades =[]
        self.passing_grade = passing_grade

    def add_student(self,student):
        self.students[student.student.id] = student
        self.grades[student.student.id] = {}

    def add_course(self,course):
        self.courses[course.course_code] = course


    def enroll_student(self,student_id,course_code):
        if student_id in self.students and course_code in self.courses:
            if course_code not in self.grades[student_id]:
                self.grades[student_id][course_code] = {}
            else:
                print("student or course not found")


