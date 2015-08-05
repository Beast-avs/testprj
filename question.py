'''
This is a Question data type. 
'''

class Question:
    description = None
    answerWeights = None
    answers = None
    
    def __init__(self, description, answers, answerWeights):
        self.description = description
        self.answers = self.validateAnswerAssignments(answers, answerWeights)
        
    def calculateAnswer(self):
        sum = 0
        for i in xrange(0,len(self.answers)-1):
            sum += float(self.answers[i])
            
        return sum/len(self.answers)
    
    def validateAnswerAssignments(self, answers, answerWeights):
        answersAssigned = None
        for i in xrange(0, len(answers)-1):
            self.answerWeights.append(float(answerWeights[i]))
        return answers
    
    def __str__(self):
        return ("Question instance has attributes:"
        "\n\tdescription: " + str(self.description) +
        "\n\tanswerWeights[" + str(self.answerWeights) + "]"
        "\n\tanswers[" + str(self.answers) + "]")