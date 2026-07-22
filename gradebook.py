
class Gradebook:
    def __init__(self,passing_grade=55):
        self.students = {}
        self.courses = {}
        self.grades ={}
        self.comments ={}
        self.passing_grade = passing_grade

    def add_student(self,student):
        self.students[student.get_id] = student
        self.grades[student.get_id] = {}

    def add_course(self,course):
        self.courses[course.course_code] = course


    def enroll_student(self,student_id,course_code):
        if student_id in self.students and course_code in self.courses:
            if course_code not in self.grades:
                self.grades[student_id] = {}
                self.grades[student_id][course_code] = {}
                self.students[student_id].enroll(course_code)
                self.courses[course_code].enroll(student_id)
            else:
                print("Student is ID enrolled")
        else:
            print("Student or course not found")


    def add_assessment(self,course_code,assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
        else:
            print("course not found")


    def record_grade(self,student_id,course_code,assessment_title,score):
        if student_id not in self.grades:
            self.grades[student_id] = {}
            if course_code not in self.grades[student_id]:
                self.grades[student_id][course_code]={}
                self.grades[student_id][course_code][assessment_title] = score
            else:
                print("Student not enrolled in course")
        else:
            print("Student or course not found")

    def calculate_average(self,student_id,course_code):
        if student_id in self.grades and course_code in self.grades[student_id]:
            score = self.grades[student_id][course_code].values()
            return sum(score)/len(score)
        else:
            return 0


    def show_report(self,student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Report for {student.name} ({student.student_id})")
            if student_id in self.grades:
                for course_code, assessment in self.grades[student_id].items():
                    average = self.calculate_average(student_id,course_code)
                    result = self.get_result(average)
                    letter= self.get_letter_grade(average)
                    print(f"Course: {course_code} , Average: {average:.2f}% , Letter Grad: {letter} , Result: {result}")
                    for assessment_title, score in assessment.items():
                        print(f"{assessment_title}: {score}")
            else:
                print("No grades recorded")
        else:
            print("student not found")

        if student_id in self.comments:
                print(f"Teacher comment : {self.comments[student_id]}")
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


    def get_letter_grade(self,average):
        if average is None:
            return "N / A"
        elif average >=90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 55:
            return "D"
        else:
            return "F"

    def add_comment(self,student_id,comment):
        if student_id in self.students:
            self.comments[student_id] = comment
            print(f"comment added {student_id}")
        else:
            print("student not found")






