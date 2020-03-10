import abc

class AbstractFactory(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_instance(self, instance_type, arguments):
        raise NotImplementedError('get_instance was not implemented')
