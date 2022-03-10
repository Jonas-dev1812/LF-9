import uuid


class User:
    def __init__(self, lastName, firstName, email):
        self.id = uuid.uuid4().hex
        self.lastName = lastName
        self.firstName = firstName
        self.email = email
    
    def _asdict(self):
        return self.__dict__


