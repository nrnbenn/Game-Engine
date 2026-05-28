from Engine.internals.saveObject import SaveObject

def save(saveObject):
    #save the saveObject to disk
    pass

def load():
    #get the saveObject from disk
    return(SaveObject())

def loadObject(data):
    return(loaders[data.objectType](data.objectType, data))

savers = {}
loaders = {}

filePath = ""