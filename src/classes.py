f = open("./data/currentClasses.txt")

canClose = False

def getClasses():
    currentClasses = []
    for x in f:
        currentClasses.insert(0, x.strip('\n'))
    canClose = True
    return currentClasses

def saveClasses(currentClasses):
    f = open("./data/currentClasses.txt", 'w')
    for x in currentClasses:
        f.write(x + '\n')
    canClose = True


if canClose == True:
    f.close()
    canClose = False
