'''
Class for Exercise data type.
'''
from question import Question

class Exercise:
    notes = ""
    questions = None
    marks = None
    timeSpent = 0
    
    def __init__(self, notes):
        self.notes = notes
        self.questions = []
    
    def getQuestions(self):
        return self.questions

    def addQuestion(self, questionDescription, answers, answerWeights):
        self.questions.append(Question(questionDescription,answers,answerWeights))
        return self
        
    