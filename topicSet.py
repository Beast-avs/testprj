'''
Contains the whole topics available in the system. It is used for keeping all the tailored content in one place.
Bonded with data storage.
'''

from topic import Topic
import json
import os

class TopicSet:
    name = None
    topics = None
    filename = '/home/ubuntu/workspace/topicSet.json'
    
    def __init__(self):
        self.name = "Default Name"
        self.topics = []
        
    def addTopic(self, topic):
        self.topics.append(topic)
        return self
        
    def saveToFile(self):
        file = None
        if not os.path.isfile(self.filename):
            file = open(self.filename, 'w')
        else: 
            file = open(self.filename, 'a+')
        json.dump(self, file, default=lambda o: o.__dict__)
        file.close()
        return self
        
    def openFromFile(self):
        file = open(self.filename, 'r')
        print json.load(file)
        return self
        
    def convertToTopics(self):
        pass