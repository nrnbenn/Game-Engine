from Engine.internals.saveLoad import savers, loaders
from Engine.internals.saveObject import SaveObject

class Parameter():
    def __init__(self, variablename, interface, value, fromSave=False):
        self.initialvalue = value
        self.value = value
        self.variablename = variablename
        self.interface = interface

        self.interface.add_parameter(self)

        self.set(value)

        if not fromSave:
            self.Initiate()

    def update(self):
        value = getattr(self.interface.parentComponent, self.variablename)
        self.value = value

    def set(self, value):
        setattr(self.interface.parentComponent, self.variablename, value)
        self.value = value

    def get(self):
        self.update()
        return(self.value)

    def Initiate(self):
        pass
