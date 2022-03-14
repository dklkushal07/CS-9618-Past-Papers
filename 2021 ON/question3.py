#completed

ArrayNodes = [[0 for _ in range(3)] for _ in range(20)] # 2d array with space for 20 nodes
RootPointer = -1 # integer that points to the first node in the binary tree
FreeNode = 0  #integer that points to the first empty node in the array

def AddNode(arrayNodes, rootPointer, freeNodePointer):
    userInputtedData = int(input("Enter the data"))
    if freeNodePointer <= 19:
        arrayNodes[freeNodePointer][0] = -1
        arrayNodes[freeNodePointer][1] = userInputtedData
        arrayNodes[freeNodePointer][2] = -1

        if rootPointer == -1:
            rootPointer = 0
        else:
            placed = False
            currentNode = rootPointer
            while not placed:
                if userInputtedData < arrayNodes[currentNode][1]:
                    if arrayNodes[currentNode][0] == -1:
                        arrayNodes[currentNode][0] = freeNodePointer
                        placed = True
                    else:
                        currentNode = arrayNodes[currentNode][0]
                else:
                    if arrayNodes[currentNode][2] == -1:
                        arrayNodes[currentNode][2] = freeNodePointer
                        placed = True
                    else:
                        currentNode = arrayNodes[currentNode][2]
        freeNodePointer += 1
    else:
        print("Array is full")
    return arrayNodes, rootPointer, freeNodePointer

def PrintAll(arrayNodes):
    for i in range(20):
        print(arrayNodes[i][0],arrayNodes[i][1],arrayNodes[i][2])

for _ in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll(ArrayNodes)

def InOrder(arrayNodes,rootPointer):
    if arrayNodes[rootPointer][0] != -1:
        InOrder(arrayNodes, arrayNodes[rootPointer][0])
    print(arrayNodes[rootPointer][1])
    if arrayNodes[rootPointer][2] != -1:
        InOrder(arrayNodes, arrayNodes[rootPointer][2])

InOrder(ArrayNodes,RootPointer)