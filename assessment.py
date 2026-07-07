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
                print("invalid score")
            elif percentage >= 90 :
                print("Excellent")
            elif percentage >= 70 :
                print("Good")
            elif percentage >= 50 :
                print("Need for effort")
            else:
                 print("Failed")


    def display_info(self):
        print(f"{self.title} - Max score: {self.max_score}")








