from Engine.internals.saveObject import SaveObject

def save(saveObject):
    #save the saveObject to disk
    pass

def load():
    #get the saveObject from disk
    return(SaveObject())

savers = {}
loaders = {}

filePath = ""