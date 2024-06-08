def readData():
    file = open("data.txt", "r")
    data = file.readlines()
    file.close()

    dataList = []
    for line in data:
        dataList.append(line.strip().split(","))
    
    return dataList