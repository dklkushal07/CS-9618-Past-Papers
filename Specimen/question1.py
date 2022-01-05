TheData = [20, 30, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for Count in range(0, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count -1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1
    return TheData
def print_TheData(TheData):
    for _ in range(len(TheData)):
        print(TheData[_])

print("Before sorting")
print_TheData(TheData)
InsertionSort(TheData)
print("After sorting")
print_TheData(TheData)


def Linear_Search(TheData):
    whole_num = int(input("Enter the whole number"))
    found = False
    for _ in range(len(TheData)):
        if whole_num == TheData[_]:
            found = True
            break
        else:
            found = False
    if found:
        print("found")
    else:
        print("not found")
    return found

Linear_Search(TheData)

