from Engine.internals.saveObject import SaveObject
from Engine.internals.peristentDataObject import PersistentDataObject, persistentDataLoaders, persistentDataSavers

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
