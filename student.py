class Student:
    def __init__(self,student_id ,nam ,email,course ):
        self.__student_id = student_id
        self.__full_name = nam
        self.__email = email
        self.course = []

    def get_id(self):
        return self.__student_id

    def get_nam(self):
        return self.__full_name

    def get_email(self):
        return self.__email

    def set_email(self,email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid Email address")


    def enroll_course(self,course_code):
        if course_code not in self.course:
            self.course.append(course_code)
        else:
            print("Student already enrolled in this course")
            


