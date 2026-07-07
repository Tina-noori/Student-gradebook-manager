from assessment import Assessment
class Quiz(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"Quiz : {self.title} - Max score: {self.max_score}")