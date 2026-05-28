from Engine.internals.saveObject import SaveObject
from Engine.internals.saveLoad import savers, loaders, loadObject

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

    def Initiate(self):
        pass