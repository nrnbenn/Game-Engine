from Engine.internals.saveObject import SaveObject
from Engine.internals.peristentDataObject import PersistentDataObject
from Engine.internals.saveLoad import savers, loaders, loadObject

class PersistentDataContainer(dict):
    def __init__(self, fromSave=False, iterable=None):
        super().__init__(iterable or {})
        if not fromSave:
            self.Initiate()

    def addPersistentData(self, dataObject, name, overrideCurrentData=False):
        if (not name in self) or ((name in self) and overrideCurrentData):
            self[name] = dataObject
            self[name].name = name

    def generateSaveObject(self):
        saveObject = SaveObject(PersistentDataContainer)
        for key in self:
            saveObject[key] = self[key].generateSaveObject()
        return(saveObject)
    
    def fromSaveObject(cls, saveObject):
        newContainer = PersistentDataContainer(fromSave=True)
        for key in saveObject:
            newContainer[key] = loadObject(saveObject[key])
        return(newContainer)

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def Initiate(self):
        pass