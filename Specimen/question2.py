class HiddenBox:
    # __BoxName private string
    # __Creator private string
    # __DateHidden private string
    # __GameLocation private string
    # __LastFinds private array 2d [10] of string
    # __Active private boolean

    def __init__(self, BoxName, Creator, DateHidden, GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__Active = False
        self.LastFinds = [[None for _ in range(2)] for __ in range(10)]

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


def NewBox(TheBoxes):
    BoxName = input("Enter the box name")
    Creator = input("Enter the creator's player name")
    DateHidden = input("Enter the date the box was created")
    GameLocation = input("Enter the location of the box")
    TheBoxes.append(HiddenBox(BoxName,Creator,DateHidden,GameLocation))


TheBoxes = [HiddenBox("", "", "", "") for _ in range(10000)]


NewBox(TheBoxes)

class PuzzleBox(HiddenBox):
    # PuzzleBox is string
    # Solution is string
    def __init__(self, PuzzleBox, Solution):
        self.PuzzleBox = PuzzleBox
        self.Solution = Solution
