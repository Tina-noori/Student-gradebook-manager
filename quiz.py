from assessment import Assessment
class Quiz(Assessment):
    def __init__(self, title, max_score):
        super().__init__(title, max_score)