from assessment import Assessment
class Quiz(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"Quiz : {self.title} - Max score: {self.max_score}")


    def grade_message(self,score):
            percentage = self.calculate_percentage(score)
            if percentage is None:
                print("Invalid score")
            elif percentage >= 90:
                print("Great quiz result")
            elif percentage >= 70:
                print("Good effort on the quiz")
            elif percentage >= 50:
                print("Needs more practice")
            else:
                print("Quiz failed")
                
