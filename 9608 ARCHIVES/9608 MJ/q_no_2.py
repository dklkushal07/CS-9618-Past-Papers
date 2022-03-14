class QuestionClass:
    def __init__(self,QuestionP,AnswerP,DifficultyP):
        self.__Question = QuestionP # string storing the question
        self.__Answer = AnswerP  #string storing the correct answer
        self.__Difficulty = DifficultyP #integer storing the difficulty (from 0 to 10)
    
    def GetQuestion(self):
        return self.__Question
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetAnswer(self):
        return self.__Answer

class QuizClass:
    
    Questions = [QuestionClass(None,None,None) for _ in range(20)]
    
    def __init__(self):
        self.NumberOfQuestions = 0
    
    def AddQuestion(self,question):
        global Questions
        Questions[self.NumberOfQuestions] = question


