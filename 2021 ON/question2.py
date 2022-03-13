from xml.etree.ElementTree import PI


class Picture:
    def __init__(self,DescriptionP,WidthP,HeightP,FrameColourP):
        self.__Description = DescriptionP # string that stores a description of a picture
        self.__Width = int(WidthP) # integer that stores the width
        self.__Height = int(HeightP) # integer that stores the height
        self.__FrameColour = FrameColourP # string that stores the colour
    
    def getHeight(self):
        return self.__Height
    
    def getDescription(self):
        return self.__Description

    def getWidth(self):
        return self.__Width
    
    def getColour(self):
        return self.__FrameColour
        
    def setDescription(self,DescriptionP):
        self.__Description = DescriptionP
    
PictureArray = [Picture("",0,0,"") for _ in range(100)]

def ReadData(PictureArray):
    filename = "Pictures.txt"
    counter = 0
    # try:
    file = open(filename,'r')
    Description = file.readline().strip().lower()
    while Description != "":
        Width = file.readline().strip()
        Height = file.readline().strip()
        FrameColour = file.readline().strip().lower()
        PictureArray[counter] = Picture(Description, Width, Height, FrameColour)
        counter += 1
        Description = file.readline().strip().lower()
    # except IOError:
    #     print("The file doesn't exist")
    return counter, PictureArray

print(ReadData(PictureArray))