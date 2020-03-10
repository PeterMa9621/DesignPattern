import abc


class UserInterface(object, metaclass=abc.ABCMeta):

    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None

    @abc.abstractmethod
    def get_role(self):
        raise NotImplementedError('must define get_name')
