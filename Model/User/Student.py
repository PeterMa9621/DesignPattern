from Interface.User.UserInterface import UserInterface


class Student(UserInterface):
    def __init__(self, name, age, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    def get_role(self):
        return 'Student'
