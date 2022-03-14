# # COULDNT SOLVE THIS QUESTION




# import os
# QueueData = ["" for _ in range(20)]
# StartPointer = 0
# EndPointer = 0


# def Enqueue(item, QueueData, EndPointer):
#     if EndPointer < 20:
#         for _ in len(QueueData):
#             if QueueData[_] != "":
#                 QueueData[_] = item
#                 EndPointer = EndPointer + 1
#                 return True, EndPointer
#     else:
#         return False, EndPointer


# def ReadFile(QueueData, EndPointer):
#     filename = input("Enter the filename")
#     if os.path.isfile(filename):
#         file = open(filename, 'r')
#         indicator = True
#         item = (file.readline).strip()
#         while indicator and item is not None:
#             indicator = Enqueue(item, QueueData, EndPointer)
#             item = (file.readline).strip()
#         if indicator == False:
#             file.close()
#             return 2, EndPointer
#         else:
#             file.close()
#             return 1, EndPointer
#     else:
#         return -1, EndPointer


# message, EndPointer = ReadFile(QueueData, EndPointer)
# if message == 2:
#     print("The queue was full")
# elif message == 1:
#     print("all data successfully read to the queue")
# else:
#     print("The text file couldn't be found")




# 2nd Attempt in solving this question using a new approach


QueueData = [None for _ in range(20)]
StartPointer = 0
EndPointer = 0

def Enqueue(itemToAdd):
    global EndPointer,QueueData
    if EndPointer == 20:
        return False
    else:
        QueueData[EndPointer] = itemToAdd
        EndPointer += 1
        return True

def ReadFile():
    filename = str(input("Enter the file path"))
    try:
        file = open(filename,'r')
        slot = True
        currentText = (file.readline()).strip()
        while slot and currentText != "":
            slot = Enqueue(currentText)
            currentText = (file.readline()).strip()
            print(QueueData)
        if slot:
            return 1
        else:
            return 2
    except IOError:
        return -1
    
returnedValue = ReadFile()
if returnedValue == 1:
    print("All the items were added to the queue")
elif returnedValue == 2:
    print("The queue was full")
else:
    print("The text file could not be found")


def Remove():
    global QueueData,StartPointer
    removed_elements = []
    if len(QueueData) >= 2 and (returnedValue == 2 or returnedValue == 1):
        for i in range(2):
            removed_elements.append(QueueData[StartPointer])
            QueueData[StartPointer] = None
            StartPointer = StartPointer + 1
        return (removed_elements[0] + " " + removed_elements[1])
    else:
        return("No Items")
    
print(Remove())