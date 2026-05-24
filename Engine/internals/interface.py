class Interface():
    def __init__(self, parentComponent):
        self.parentComponent = parentComponent
        self.parameters = []

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def update(self):
        for parameter in self.parameters:
            parameter.update()
