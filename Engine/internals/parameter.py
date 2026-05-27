from Engine.internals.saveLoad import savers, loaders
from Engine.internals.saveObject import SaveObject

class Parameter():
    def __init__(self, variablename, interface, value):
        self.initialvalue = value
        self.value = value
        self.variablename = variablename
        self.interface = interface

        self.interface.add_parameter(self)

        self.set(value)

    def update(self):
        value = getattr(self.interface.parentComponent, self.variablename)
        self.value = value

    def set(self, value):
        setattr(self.interface.parentComponent, self.variablename, value)
        self.value = value

    def get(self):
        self.update()
        return(self.value)
    
    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def generateSaveObject(self):
        return(SaveObject())

    def fromSaveObject(self, saveObject):
        pass
