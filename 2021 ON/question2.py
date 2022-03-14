#completed


class Picture:
    #constructor
    def __init__(self,DescriptionP,WidthP,HeightP,FrameColourP):
        self.__Description = DescriptionP # string that stores a description of a picture
        self.__Width = int(WidthP) # integer that stores the width
        self.__Height = int(HeightP) # integer that stores the height
        self.__FrameColour = FrameColourP # string that stores the colour
    
    #getter and setter methods
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


#Creating an array of 100 objects of type Picture    
PictureArray = [Picture("",0,0,"") for _ in range(100)]


def ReadData(PictureArray):
    counter = 0
    try:
        file = open(r"C:\Users\dklku\Desktop\CS-9618-Past-Papers\2021 ON\Pictures.txt",'r')
        Description = file.readline().strip().lower()
        while Description != "":
            Width = file.readline().strip()
            Height = file.readline().strip()
            FrameColour = file.readline().strip().lower()
            PictureArray[counter] = Picture(Description, Width, Height, FrameColour)
            counter += 1
            Description = file.readline().strip().lower()
    except IOError:
        print("The file doesn't exist")
    return counter, PictureArray
# the function ReadData is called such that it returns counter and PictureArray
ReadData(PictureArray)

UserInputted = Picture(None,\
    int(input("Enter the width")),\
        int(input("Enter the height")),\
            (input("Enter the colour")).lower())


for i in range(0,99,1):
    if UserInputted.getWidth() >= PictureArray[i].getWidth() \
        and UserInputted.getHeight() >= PictureArray[i].getHeight() \
            and UserInputted.getColour() == PictureArray[i].getColour():
                UserInputted.setDescription(PictureArray[i].getDescription())
                print("found",PictureArray[i].getDescription(),\
                    "with",PictureArray[i].getHeight(),"height",\
                        PictureArray[i].getWidth(),"width",\
                            "and",PictureArray[i].getColour(),"colour")
                       