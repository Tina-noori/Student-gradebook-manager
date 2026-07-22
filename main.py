# test

from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook


gradebook = Gradebook()

def main_menu():


    global gradebook
    while True:
        print("\n====Student Gradebook Manager====")
        print("1. Add Student")
        print("2. View Student")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Add Assignment")
        print("6. Record Grade")
        print("7. View Student Report")


        choice = input("Choice an option: ")
        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            student = Student(student_id, name, email,)
            gradebook.add_student(student)
            print(f"Student {name} added successfully!")
        elif choice == "2":
            print("\n====Student List====")
            for student in gradebook.students.values():
                print(f"{student.get_id()} - {student.get_name()} - {student.get_email()}")
        elif choice == "3":
            code = input("Enter Course Code: ")
            name = input("Enter Course Name: ")
            course = Course(code, name)
            gradebook.add_course(course)
            print(f"Course {name} added successfully!")
        elif choice == "4":
            student_id =input("Enter Student ID: ").lower()
            course_code =input("Enter Course Code: ").upper()
            if student_id in gradebook.students and course_code in gradebook.courses:
               print(f"Student {student_id} enrolled in course {course_code} successfully!")

        elif choice == "5":
            course_code =(input("Enter Course Code: "))
            title = input("Enter Course Title: ")
            max_score = int(input("Enter Maximum Score:"))
            assessment_type = input("Type (quiz/exam/project): )").lower()
            if assessment_type == "quiz":
                assessment=Quiz(title, max_score)
            elif assessment_type == "exam":
                assessment=Exam(title, max_score)
            elif assessment_type == "project":
                assessment=Project(title, max_score)
            else:
                print("Invalid Assessment Type")

            gradebook.courses[course_code].add_assessment(assessment)
            print(f"Assessment {title} added to course {course_code}!")
        elif choice == "6":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            title = input("Enter Assessment Title: ")
            score = int(input("Enter Score: "))
            gradebook.record_grade(student_id, course_code,title ,score)

        elif choice == "7":
            student_id = input("Enter Student ID: ").strip()
            if student_id in gradebook.students:
                student = gradebook.students[student_id]
                print("====Student Report====")
                print(f"Student ID: {student.get_id()}")
                print(f"Name: {student.get_name()}")
                print(f"Email: {student.get_email()}")
            else:
                print("Student not found.")
        else:
            print("Invalid Choice")





        for course_code, course in gradebook.courses.items():
            print(f"\nCourse: {course_code} - {course.course_name}")
            print("Grades:")
            if student_id in gradebook.grades and course_code in gradebook.grades[student_id]:
                percents =[]
                for assessment in course.assessments:
                    if assessment.title in gradebook.grades[student_id][course_code]:
                        gradebook=gradebook.grades[student_id][course_code][assessment.title]
                        percent = (gradebook , assessment.max_score) * 100
                        percents.append(percent)
                        letter = gradebook.get_letter_grade(percent)
                        print(f"{assessment.title}: {gradebook}/{assessment.max_score} = {percent:.2f}% {letter}")
                    else:
                        print(f"{assessment.title}: No gradebook recorded ")
                    if percents :
                        avg = sum(percents) / len(percents)
                        result =gradebook.get_result(avg)
                        letter_avg = gradebook.get_letter_grade(avg)

                        print(f"\nAverage:{avg:.2f}% ")
                        print(f"Result: {result}")
                        print(f"Letter: {letter_avg}")
                else:
                    print("Student not found.")
            else:
                print("No gradebook recorded yet.")



if __name__ == "__main__":
    main_menu()












