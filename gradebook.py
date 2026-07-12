
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

    def add_assessment(self,course_code,assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
        else:
            print("course not found")


    def record_grade(self,student_id,course_code,assessment_title,score):
        if student_id in self.students and course_code in self.courses:
            if course_code in self.grades[student_id]:
                self.grades[student_id][course_code][assessment_title] = score
            else:
                print("Student not enrolled in course")
        else:
            print("Student or course not found")

    def calculate_average(self,student_id,course_code):
        if student_id in self.grades and course_code in self.grades[student_id]:
            score = list(self.grades[student_id][course_code].values())
            if score :
                return sum(score)/len(score)
            return None

    def show_report(self,student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Report for {student.name} ({student.student_id})")
            if student_id in self.grades:
                for course_code, assessment in self.grades[student_id].items():
                    average = self.calculate_average(student_id,course_code)
                    result = self.get_result(average)
                    print(f"{course_code} Average: {average}, Result: {result}")
                    for assessment_title, score in assessment.items():
                        print(f"{assessment_title}: {score}")
            else:
                print("student not found")


    def search_student(self,keyword):
        for student_id,student in self.students.items():
            if keyword.lower() in student_id.lower() or keyword.lower() in student.name.lower():
                print(f"Found : {student.name} ({student.id})")
                return student
            print("student not found")
            return None


    def delete_student(self,student_id):
        if student_id in self.students:
            del self.students[student_id]
            if student_id in self.grades:
                del self.grades[student_id]
                print(f"Student {student_id} remove from gradebook")
            else:
                print("student not found")


    def get_result(self,average):
        if average is None:
            return "No grades"
        elif average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"






