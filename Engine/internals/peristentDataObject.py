from Engine.internals.saveObject import SaveObject
from Engine.internals.saveLoad import savers, loaders

class PersistentDataObject():
    def __init__(self, name, value, fromSave=False):
        self.value = value
        self.name = name

        if not fromSave:
            self.Initiate()

    def Initiate(self):
        pass

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def generateSaveObject(self):
        save = SaveObject(PersistentDataObject)
        #name
        save["name"] = self.name
        save["value"] = f"THIS PERSISTENT DATA OBJECT HAS NOT OVERIDDEN GENERATESAVEOBJECT(). "
        return(save)

    def fromSaveObject(cls, saveObject):
        newObject = PersistentDataObject("", "", fromSave=True)
        newObject.name = saveObject["name"]
        newObject.value = (str(saveObject["value"]) + "THIS PERSISTENT DATA OBJECT HAS NOT OVERRIDEN FROMSAVEOBJECT(). ")