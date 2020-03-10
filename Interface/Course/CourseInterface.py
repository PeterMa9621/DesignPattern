import abc
from Interface.User.UserInterface import UserInterface

class CourseInterface(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_course_name(self):
        raise NotImplementedError('get_course_name was not implemented')

    @abc.abstractmethod
    def get_course_code(self):
        raise NotImplementedError('get_course_code was not implemented')

    @abc.abstractmethod
    def get_members(self):
        raise NotImplementedError('get_students was not implemented')

    @abc.abstractmethod
    def add_member(self, member):
        raise NotImplementedError('add_member was not implemented')

    @abc.abstractmethod
    def remove_member(self, member):
        raise NotImplementedError('remove_member was not implemented')

    @abc.abstractmethod
    def set_school(self, school):
        raise NotImplementedError('set_school was not implemented')

    @abc.abstractmethod
    def get_school(self):
        raise NotImplementedError('get_school was not implemented')
