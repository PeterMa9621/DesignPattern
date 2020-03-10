from Interface.User.UserInterface import UserInterface


class Tutor(UserInterface):
    def __init__(self, name, age, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    def get_role(self):
        return 'Tutor'
