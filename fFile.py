def readFileIntoAr(fName):
    #print(fName)
    with open(fName, 'r') as file:
        lines = [line.rstrip() for line in file] 
    return lines
def writeIntoFile(content, fName):
    f = open(fName, "w")
    f.write(content)
    f.close()
def writeArrIntoFile(data, fName):
    with open(fName, "w") as txt_file:
        for line in data:
            txt_file.write(line + "\n")
