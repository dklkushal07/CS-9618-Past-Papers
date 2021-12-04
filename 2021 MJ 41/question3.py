# class TreasureChest:
#     def __init__(self, questionP, answerP, pointsP):
#         # question : private string attribute
#         # answer : private integer attribute
#         # points : private integer attribute
#         self.__question = questionP
#         self.__answer = answerP
#         self.__points = pointsP
#
#     def getQuestion(self):
#         return self.__question

def readData():
    filename = "TreasureChestData.txt"
    try:
        file = open(filename,"r")
        dataFetched = (file.readline()).strip()
    except IOError:
        print("The file is not found")