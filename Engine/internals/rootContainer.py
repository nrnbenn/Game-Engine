from Engine.internals.interface import Interface
from Engine.internals.persistentDataContainer import PersistentDataContainer
from Engine.internals.saveObject import SaveObject
from Engine.internals.saveLoad import savers, loaders, loadObject
from editorEntry import reload

class RootContainer():
    def __init__(self, fromSave=False):
        self.children = []
        self.killScheduleQueue = []

        self.interface = Interface(self)
        self.persistentDataContainer = PersistentDataContainer()

        self.running = False
        self.game_running = False
        self.game_is_paused = False

        self.rootUiUpdate = None

        if not fromSave:
            self.Initiate()

    def Awake(self):
        pass
    def Start(self):
        pass
    def Tick(self):
        pass
    def Update(self):
        #do scheduled killing
        for kill in self.killScheduleQueue:
            kill.parent.remove_child(kill)
    def Stop(self):
        pass
    def Initiate(self):
        pass

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
        while not len(toSearch) == 0:
            popped = toSearch.pop()
            results.append(popped)
            if recursive:
                newSearches = popped.getAllChildren()
                for newSearch in newSearches:
                    toSearch.append(newSearch)
        return(results)

    def Instantiate(self, component, name=None, parent=None):
        newComponent = component(self)
        self.add_child(newComponent)
        if name:
            newComponent.set_name(name)
        if parent:
            newComponent.set_parent(parent)
        return(newComponent)

    def scheduleForKilling(self, component):
        self.killScheduleQueue.append(component)

    def MainLoop(self):
        self.rootUiUpdate() #update the root ui
        game_started = False #used to know if to send Start()
        self.performOnAllChildren(lambda c: c.Awake()) #send Awake()
        self.Awake()
        while self.running:
            self.performOnAllChildren(lambda c: c.Tick()) #send Tick()
            self.Tick()
            if self.game_running and (not self.game_is_paused): #if ticking needs to happen
                if not game_started:
                    game_started = True
                    self.performOnAllChildren(lambda c: c.Start()) #send Start()
                    self.Start()
                self.performOnAllChildren(lambda c: c.Update()) #send Update()
                self.Update()
            elif not self.game_is_paused: #if ticking does not happen but the game is not paused (aka. if the game stops)
                self.performOnAllChildren(lambda c: c.Stop()) #send Stop()
                self.Stop()
                game_started = False

    def performOnAllChildren(self, action):
        allChildren = self.getAllChildren(recursive=True)
        for child in allChildren:
            action(child)

    def StartMainLoop(self):
        self.running = True
        self.MainLoop()
    def StopMainLoop(self):
        self.game_running = False
        self.running = False
        reload(withSaveObject=self.generateSaveObject())
    def StartGame(self):
        self.game_running = True
    def StopGame(self):
        self.game_running = False
    def PauseGame(self):
        self.game_is_paused = True
    def ResumeGame(self):
        self.game_is_paused = False

    def __init_subclass__(cls): #called when a class that inherits from this object is defined
        pass
        #register data serializers
        savers[cls] = cls.generateSaveObject
        loaders[cls] = cls.fromSaveObject

    def generateSaveObject(self):
        save = SaveObject(RootContainer)
        
        #children
        save["children"] = []
        for child in self.children:
            save["children"].append(child.generateSaveObject())
        #interface is not saved (see component.py)
        #persistentDataContainer
        save["peristentDatContainer"] = self.persistentDataContainer.generateSaveObject()

    def fromSaveObject(cls, saveObject):
        newRootContainer = RootContainer(fromSave=True)
        #name
        for childSaveObject in saveObject["children"]:
            newChild = loadObject(childSaveObject)
            newChild.parent = newRootContainer #set the parent of the new child to the new rootcontainer as parents are done on the 'layer' before
            newRootContainer.children.append(newChild)
        #persistentDataContainer
        newRootContainer.persistentDataContainer = loadObject(saveObject["persistentDataContainer"])
        return(newRootContainer)