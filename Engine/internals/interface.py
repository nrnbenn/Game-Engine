from Engine.internals.saveObject import SaveObject
from Engine.internals.saveLoad import savers, loaders

class Interface():
    def __init__(self, parentComponent, fromSave=False):
        self.parentComponent = parentComponent
        self.parameters = []

        if not fromSave:
            self.Initiate()

    def add_parameter(self, parameter):
        self.parameters.append(parameter)
        parameter.interface = self

    def update(self):
        for parameter in self.parameters:
            parameter.update()

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def generateSaveObject(self):
        return(SaveObject())

    def fromSaveObject(self, saveObject):
        return(Interface(None, True))

    def Initiate(self):
        pass