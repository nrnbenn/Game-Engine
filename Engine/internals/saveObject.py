class SaveObject(dict):
    def __init__(self, objectType, iterable=None):
        super().__init__(iterable or {})
        self.objectType = objectType