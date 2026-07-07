class Assessment:
    def __init__(self, title,max_score):
        self.title = title
        self.max_score = max_score


    def calculate_percentage(self,score):
        if 0 <= score <= self.max_score:
            return (score/self.max_score)*100
        return None

    def grade_message(self,score):
            percentage = self.calculate_percentage(score)
            if percentage is  None:
                return "invalid score"
            elif percentage >= 90 :
                return "Excellent"
            elif percentage >= 70 :
                return "Good"
            elif percentage >= 50 :
                return "Need for effort"
            else:
                 return "Failed"


    def display_info(self):
        print(f"{self.title} - Max score: {self.max_score}")








