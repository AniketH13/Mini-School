class User:
    def __init__(self, id, name, role, email):
        self.id = id
        self.name = name
        self.role = role  # admin, teacher, parent
        self.email = email
