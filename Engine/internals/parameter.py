class Parameter():
    def __init__(self, variablename, interface, value):
        self.initialvalue = value
        self.value = value
        self.variablename = name
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
