from Engine.internals.interface import Interface

class Component():
    def __init__(self, parent):
        self.name = self.__name__
        self.children = []
        self.parent = parent
        self.rootContainer = parent
        self.interface = Interface(self)

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def set_parent(self, parent):
        self.parent.remove_child(self)
        self.parent = parent
        self.parent.add_child(self)

    def set_name(self, newname):
        self.name = newname

    def Start(self):
        pass
    def Tick(self):
        self.interface.update()

    def getChildByName(self, name, recursive=False): #returns first one it finds
        result = self.getChildrenByName(name, recursive=recursive)
        if len(result) == 0:
            return(None)
        return(result[0])

    def getChildByType(self, type, recursive=False): #returns first one it finds
        result = self.getChildrenByType(type, recursive=recursive)
        if len(result) == 0:
            return(None)
        return(result[0])

    def getChildrenByName(self, name, recursive=False): #returns all in a list
        toSearch = self.children
        results = []

        while not len(toSearch) == 0:
            search = toSearch.pop()
            if search.name == name:
                results.append(search)
            if recursive:
                newSearches = search.getAllChildren()
                for newSearch in newSearches:
                    toSearch.append(newSearch)

        return(results)

    def getChildrenByType(self, type, recursive=False): #returns all in a list
        toSearch = self.children
        results  = []
        while not len(toSearch) == 0:
            search = toSearch.pop()
            if type(search) == type:
                results.append(search)
            if recursive:
                newSearches = search.getAllChildren()
                for newSearch in newSearches:
                    toSearch.append(newSearch)

    def getAllChildren(self, recursive=False):
        results = []
        toSearch = self.children
        while not len(toSearch) = 0:
            popped = toSearch.pop()
            results.append(popped)
            if recursive:
                newSearches = popped.getAllChildren()
                for newSearch in newSearches:
                    toSearch.append(newSearch)
        return(results)
