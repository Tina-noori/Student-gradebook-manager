# test

from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook
gradebook = Gradebook()

# step 1 : Add a student

student_1 = Student("S001","Sina Noori","sina1212@gmail.com",[])
gradebook.add_student(student_1)

# step 2 : Add a Course
course_1 = Course("PY101","Python Programming")
gradebook.add_course(course_1)



#step 3 : Enroll the Student in the Course
gradebook.enroll_student(student_1.get_id(),course_1.course_code)
course_1.add_student(student_1)

#step 4 : Add assessment
quiz_1 = Quiz("Quiz 1",10)
exam_1 = Exam("Midterm Exam",100)
project_1 = Project("Final Project",100)

course_1.add_assessment(quiz_1)
course_1.add_assessment(exam_1)
course_1.add_assessment(project_1)

# step 5 : Record Gradebook
gradebook.record_grade(student_1.get_id(),course_1.course_code,quiz_1.title,8)
gradebook.record_grade(student_1.get_id(),course_1.course_code,exam_1.title,75)
gradebook.record_grade(student_1.get_id(),course_1.course_code,project_1.title,90)

#step 6 : Calculate Average

average = gradebook.calculate_average(student_1.get_id(),course_1.course_code)
letter_avg = gradebook.get_letter_grade(average)


#step 7 : Show Record
print("\n===== Student Report =====")
print(f"Student ID: {student_1.get_id()}")
print(f"Name:{student_1.get_nam()}")
print(f"Email:{student_1.get_email()}")
print(f"\nCourse:{course_1.course_name}-{course_1.course_name}")
print("\nGrades:")
for assessment in course_1.assessments:
    if assessment.title in gradebook.grades[student_1.get_id()][course_1.course_code]:
        grade = gradebook.grades[student_1.get_id()][course_1.course_code][assessment.title]
        percent =(grade/assessment.max_score)*100
        letter = gradebook.get_letter_grade(percent)
        print(f"{assessment.title}: {grade} / {assessment.max_score}={percent:.0f}%({letter})")
    else:
        print(f"{assessment.title}:No grade recorded")



print(f"\nAverage: {average:.2f}%({letter_avg})")
if average >= 50:
    print(f"Result: Passed")
else:
    print("Result: Failed")

comment=gradebook.add_comment(student_1.get_id(),"Great improvement,keep practicing")
if student_1.get_id() in gradebook.comments:
    print(f"Teacher Comment: {gradebook.comments[student_1.get_id()]}:")
else:
    print(f"Teacher Comment:No comment available")


