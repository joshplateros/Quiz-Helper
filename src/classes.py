f = open("./data/currentClasses.txt", "r")

canClose = False

def getClasses():
    currentClasses = []
    for x in f:
        currentClasses.append(x)
    canClose = True
    return currentClasses

if canClose == True:
    f.close()
