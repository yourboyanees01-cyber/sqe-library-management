class Student:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        """Add a score to the student's record. Raises ValueError if score is negative."""
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)