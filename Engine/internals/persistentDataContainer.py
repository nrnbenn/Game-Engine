from Engine.internals.saveObject import SaveObject
from Engine.internals.peristentDataObject import PersistentDataObject
from Engine.internals.saveLoad import savers, loaders

class PersistentDataContainer(dict):
    def addPersistentData(self, dataObject, name):
        self[name] = dataObject
        self[name].name = name

    def generateSaveObject(self):
        saveObject = SaveObject()
        for key in self:
            saveObject[key] = self[key]
        return(saveObject)
    
    def fromSaveObject(self, saveObject):
        pass

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject