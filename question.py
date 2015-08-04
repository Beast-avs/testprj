'''
This is a Question data type. 
'''

class Question:
    
    answers = ['0.0','0.2','0.8','1.0']
    
    def calculateAnswer(self):
        sum = 0
        for i in xrange(0,len(self.answers)-1):
            sum += float(self.answers[i])
            
        return sum/len(self.answers)
    
    
a = Question()
print a.calculateAnswer()
