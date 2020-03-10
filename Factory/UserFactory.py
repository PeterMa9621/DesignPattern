from Factory.Student import Student
from Factory.Tutor import Tutor
from Factory.UserInterface import UserInterface


class RoleTypeError(Exception):
    pass


class UserFactory(object):
    def __init__(self):
        pass

    def get_user(self, role, name, age, gender) -> UserInterface:
        if role == 'student':
            return Student(name, age, gender)
        elif role == 'tutor':
            return Tutor(name, age, gender)
        else:
            raise RoleTypeError
