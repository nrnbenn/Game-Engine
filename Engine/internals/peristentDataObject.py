from Engine.internals.saveObject import SaveObject
from Engine.internals.saveLoad import savers, loaders

class PersistentDataObject():
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def generateSaveObject(self):
        return(SaveObject())

    def fromSaveObject(self, saveObject):
        pass