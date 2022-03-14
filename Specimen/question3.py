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

