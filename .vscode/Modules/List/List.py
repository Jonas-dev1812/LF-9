import uuid


class TodoList: 
    def __init__(self, name):
        self.id = uuid.uuid1().hex
        self.name = name

    def _asdict(self):
        return self.__dict__