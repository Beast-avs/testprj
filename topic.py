'''
'''
from exercise import Exercise

class Topic:
    name = agenda = estimatedTime = progress = lectures = exercises = None
    
    def __init__(self, name, estimatedTime):
        self.name = "Simple topic"
        self.agenda = "A short description of the topic for a subject. What is disclosed here, what theories it covers, etc."
        self.estimatedTime = 0
        self.progress = 0
        self.estimatedTime = estimatedTime
        self.theories = []
        self.exercises = []
        
    
    def addTheory(self, lecture):
        self.theories.append(lecture)
        return self
    
    def getLectures(self):
        return self.lectures
        
    def addExercise(self, exercise):
        self.exercises.append(exercise)
        return self
    