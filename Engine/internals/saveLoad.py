from Engine.internals.saveObject import SaveObject

def save(saveObject, filePath):
    if filePath:
        pass

def load(filePath):
    #get the saveObject from disk
    return(SaveObject())

def loadObject(data):
    return(loaders[data.objectType](data.objectType, data))

savers = {}
loaders = {}