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
        
    def __init__(self):
        self.NumberOfQuestions = 0
        self.Questions = [QuestionClass(None,None,None) for _ in range(20)]
    def AddQuestion(self,question):
        if self.NumberOfQuestions < 20:
            self.Questions[self.NumberOfQuestions] = question
            self.NumberOfQuestions += 1
            return True
        else:
            return False

FirstQuiz = QuizClass()
Question1 = QuestionClass("What is 100/5?","20",1)
FirstQuiz.AddQuestion(Question1)   

