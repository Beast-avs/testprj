'''
'''
from exercise import Exercise

class Topic:
    name = "Simple topic"
    agenda = "A short description of the topic for a subject. What is disclosed here, what theories it covers, etc."
    estimatedTime = 0
    progress = 0
    lectures = None
    exercises = None
    
    def __init__(self, name, estimatedTime):
        self.progress = 0
        self.estimatedTime = estimatedTime
        self.lectures = []
        self.exercises = []
    
    def addLecture(self, lecture):
        self.lectures.append(lecture)
        return self
    
    def getLectures(self):
        return self.lectures
        
    def addExercise(self, exercise):
        self.exercises.append(exercise)
        return self
    
    def __str__(self):
        exes = ""
        for i in self.exercises:
            exes += str(i.getQuestions()) + ", "
            
        return ("Topic instance has attributes:"
        "\n\tname: " + str(self.name) +
        "\n\tagenda: " + str(self.agenda) +
        "\n\testimatedTime: " + str(self.estimatedTime) +
        "\n\tprogress: " + str(self.progress) +
        "\n\tlectures[ " + str(self.lectures) + "]" +
        "\n\texercises[" + exes + "]")