from Engine.internals.saveObject import SaveObject
from Engine.internals.peristentDataObject import PersistentDataObject
from Engine.internals.saveLoad import savers, loaders

class PersistentDataContainer(dict):
    def addPersistentData(self, dataObject, name, fromSave=False):
        self[name] = dataObject
        self[name].name = name

        if not fromSave:
            self.Initiate()

    def generateSaveObject(self):
        saveObject = SaveObject()
        for key in self:
            saveObject[key] = self[key]
        return(saveObject)
    
    def fromSaveObject(self, saveObject):
        return(PersistentDataContainer(None, None, True))

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def Initiate(self):
        pass