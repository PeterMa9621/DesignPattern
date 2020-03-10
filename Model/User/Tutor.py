from Interface.User.UserInterface import UserInterface


class Tutor(UserInterface):
    def __init__(self, name, age, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.subordinate = []

    def get_role(self):
        return 'Tutor'

    def add_subordinate(self, tutor):
        self.subordinate.append(tutor)

    def get_subordinate(self):
        return self.subordinate

    def remove_subordinate(self, tutor):
        self.subordinate.remove(tutor)

    def has_subordinate(self):
        return True if len(self.subordinate) != 0 else False
