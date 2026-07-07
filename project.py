from assessment import Assessment
class Project (Assessment):
    def __init__(self, title,max_score):
        super().__init__(title,max_score)


    def display_info(self):
        print(f"Project: {self.title} - Max Score: {self.max_score}")


    def grade_message(self,score):
        percentage =self.calculate_percentage(score)
        if percentage is None:
            return "Invalid Score"
        elif percentage >= 90 :
            return "Excellent project"
        elif percentage >= 55 :
            return "Project Complete"
        else:
            return "Project needs improvement"