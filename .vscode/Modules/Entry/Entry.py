from List.List import TodoList
import uuid

class Entry: 
    def __init__(self, text, todolist: TodoList, user):
        self.id = uuid.uuid3().hex
        self.text = text
        self.todolist = todolist
        self.user = user

    def _asdict(self):
        return self.__dict__