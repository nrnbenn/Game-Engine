class Component():
    def __init__(self, parent):
        self.children = []
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def set_parent(self, parent)
        self.parent.remove_child(self)
        self.parent = parent
        self.parent.add_child(self)

    def Start(self):
        pass
    def Tick(self):
        pass
