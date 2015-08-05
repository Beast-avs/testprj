'''
This is a Question data type. 
'''

class Question:
    description = None
    answerWeights = None
    answers = None
    
    def __init__(self, description, answers, answerWeights):
        self.answerWeights = []
        self.description = description
        self.answers = self.validateAnswerAssignments(answers, answerWeights)
        
    def calculateAnswer(self):
        sum = 0
        for i in xrange(0,len(self.answers)-1):
            sum += float(self.answers[i])
            
        return sum/len(self.answers)
    
    def validateAnswerAssignments(self, answers, answerWeights):
        self.answerWeights = map (lambda x: float(x), answerWeights[0:len(answers)])
        self.answerWeights[len(answerWeights):] = [float(0)]*(len(answers)-len(answerWeights))

        return map(lambda x: str(x), answers)
    