from AbstractFactory.AbstractFactory import AbstractFactory
from Model.User.Student import Student
from Model.User.Tutor import Tutor
from Interface.User.UserInterface import UserInterface


class RoleTypeError(Exception):
    pass


class UserFactory(AbstractFactory):
    def __init__(self):
        pass

    def get_instance(self, instance_type, arguments) -> UserInterface:
        role = instance_type
        name = arguments[0]
        age = arguments[1]
        gender = arguments[2]

        if role == 'student':
            return Student(name, age, gender)
        elif role == 'tutor':
            return Tutor(name, age, gender)
        else:
            raise RoleTypeError
