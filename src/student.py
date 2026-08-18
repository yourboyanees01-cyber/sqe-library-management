class Student:
    def __init__(self):
        self.scores = []

    def add_score(self, new_score):
        """Add a score to the student's record. Raises ValueError if score is negative."""
        if not isinstance(new_score, (int, float)):
            raise TypeError("Score must be a number")
        if new_score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(new_score)