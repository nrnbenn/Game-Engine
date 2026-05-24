class RootContainer():
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

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
        search = toSearch.pop()
            if search.name == name:
                results.append(search)
            if recursive:
                newSearches = search.getAllChildren()
                for newSearch in newSearches:
                    toSearch.append(newSearch)

    def getAllChildren(self):
        results = self.children
        for child in results:
            grandChildren = child.getAllChildren()
            for grandchild in grandChildren:
                results.append(grandchild)

