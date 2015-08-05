'''
Test of Topic class with related Question and Exercise
'''

from topic import Topic
from exercise import Exercise
import json 

print "Test for Topic..."

mainTopic = Topic("Simple Topic A", 3600)
mainTopic.addTheory("Simple theory about the Topic A of the Subject.")
mainTopic.addTheory("Complex theory about the Topic A of the Subject.")
ex0 = Exercise("Notes for Exercise 0")
ex0.addQuestion("Question 0.1", ["1"],  [1.0])
ex1 = Exercise("Notes for Exercise 1")
ex1.addQuestion("Question 1.1", ["one", "two", "three", "four"],  [0.0, 0.2, 1, "0.5"])
ex1.addQuestion("Question 1.2", ["one", "two"],  [1.0]).addQuestion("Question 1.3", [1,2,3,4,5,6,7,8,9], [1,0.3,0.4])
ex2 = Exercise("Notes for Exercise 2")
ex2.addQuestion("Question 2.1", ["1", "2", "3"],  [0.0, 1.0])
ex3 = Exercise("Notes for Exercise 3")
ex4 = Exercise("Notes for Exercise 4")
ex4.addQuestion("Question 4.1", ["1"],  [1.0, 0.0])
ex5 = Exercise("Notes for Exercise 5")
ex6 = Exercise("Notes for Exercise 6")
ex7 = Exercise("Notes for Exercise 7")

mainTopic.addExercise(ex0).addExercise(ex1).addExercise(ex2).addExercise(ex3)
mainTopic.addExercise(ex4).addExercise(ex5).addExercise(ex6).addExercise(ex7)


print json.dumps(mainTopic, default=lambda o: o.__dict__,sort_keys=True, indent=4)