class TreasureChest:
    def __init__(self, questionP, answerP, pointsP):
        # question : private string attribute
        # answer : private integer attribute
        # points : private integer attribute
        self.__question = questionP
        self.__answer = answerP
        self.__points = pointsP

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answerP):
        if int(self.__answer) == answerP:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0


def readData():
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        dataFetched = (file.readline()).strip()
        global arrayTreasure
        arrayTreasure = [TreasureChest(None, None, None) for xyz in range(5)]
        counter = 0
        while dataFetched:
            question = dataFetched
            global answer
            answer = (file.readline()).strip()
            points = (file.readline()).strip()
            arrayTreasure[counter] = TreasureChest(question, answer, points)
            counter += 1
            dataFetched = (file.readline()).strip()

        file.close()
    except IOError:
        print("The file is not found")


readData()
choice = int(input("Enter a treasure chest to open"))
if 0 < choice < 6:
    result = False
    attempts = 0
    while not result:
        answer = int(input(arrayTreasure[choice - 1].getQuestion()))
        result = arrayTreasure[choice - 1].checkAnswer(answer)
        attempts = attempts + 1
    print("You got", arrayTreasure[choice - 1].getPoints(attempts), "points")
