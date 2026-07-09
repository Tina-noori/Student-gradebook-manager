
class Gradebook:
    def __init__(self,passing_grade=55):
        self.students = []
        self.courses = []
        self.grades =[]
        self.passing_grade = passing_grade

    def add_student(self,student):
        self.students[student.student.id] = student
        self.grades[student.student.id] = {}
