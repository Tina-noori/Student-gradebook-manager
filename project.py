from assessment import Assessment
class Project (Assessment):
    def __init__(self, title,max_score):
        super().__init__(title,max_score)


    def display_info(self):
        print(f"Project: {self.title} - Max Score: {self.max_score}")