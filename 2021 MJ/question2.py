# Question no 2

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(searchValue):
    for x in range(0, 10):
        if arrayData[x] == searchValue:
            return True
    return False


searchValue = int(input("Enter the integer to search in the list: "))
output = linearSearch(searchValue)
if output:
    print("The integer was found")
else:
    print("The integer wasn't found")

# Bubble sort part

def bubbleSort():
    temp = None
    for x in range(len(theArray)):
        for y in range(len(theArray)-1):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y],theArray[y+1]= theArray[y+1],temp

