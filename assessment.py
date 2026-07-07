class Assessment:
    def __init__(self, title,max_score):
        self.title = title
        self.max_score = max_score
        self.students_score = {}

    def calculate_score(self,student_id,score):
        if 0 <= score <= self.max_score:
            self.students_score[student_id] = score
        else:
            print("Invalid score")
