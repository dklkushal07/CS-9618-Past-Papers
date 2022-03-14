from dataclasses import dataclass


class node:
    def __init__(self,data,nextNode = -1):
        self.data = data  #integer
        self.nextNode = nextNode  #integer

linkedList = [
    node(1,1),
    node(5,4),
    node(6,7),
    node(7,-1),
    node(2,2),
    node(0,6),
    node(0,8),
    node(56,3),
    node(0,9),
    node(0,-1)]

startPointer = 0
emptyList = 5

def outputNodes(LinkedList, StartPointer):
    if StartPointer != -1:
        print((LinkedList[StartPointer]).data)
        outputNodes(LinkedList,(LinkedList[StartPointer]).nextNode)

outputNodes(linkedList,startPointer)

def addNode(LinkedList,StartPointer,EmptyList):
    userInputtedData = int(input("Enter the data to be added at the end of the linkedList"))
    if emptyList > 0 and emptyList >9 :
        return False
    else:
        LinkedList[EmptyList] = node(userInputtedData)
        prevPointer = 0
        while StartPointer != -1:
            prevPointer = StartPointer
            StartPointer = LinkedList[StartPointer].nextNode
        LinkedList[prevPointer].nextNode = EmptyList
        return True

if addNode(linkedList,startPointer,emptyList):
    print("added a node")
else:
    print("couldnt add node")
outputNodes(linkedList,startPointer)