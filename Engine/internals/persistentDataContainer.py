from Engine.internals.saveObject import SaveObject
from Engine.internals.peristentDataObject import PersistentDataObject, persistentDataLoaders, persistentDataSavers

class PersistentDataContainer(dict):
    def addPersistentData(self, name, data):
        self[name] = PersistentDataObject(name, data)

    def generateSaveObject(self):
        saveObject = SaveObject()
        for key in self:
            saveObject[key] = self[key]
        return(saveObject)
    
    def fromSaveObject(self, saveObject):
        pass
