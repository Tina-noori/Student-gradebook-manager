class Assessment:
    def __init__(self, title,max_score):
        self.title = title
        self.max_score = max_score


    def calculate_percentage(self,score):
        if 0 <= score <= self.max_score:
            return (score/self.max_score)*100
        return None

    deff






