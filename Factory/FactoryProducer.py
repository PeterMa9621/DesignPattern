from AbstractFactory.AbstractFactory import AbstractFactory
from Factory.Course.CourseFactory import CourseFactory
from Factory.User.UserFactory import UserFactory


class FactoryTypeError(Exception):
    pass


class FactoryProducer(object):
    @staticmethod
    def get_factory(factory_name, school='UA') -> AbstractFactory:
        if factory_name == 'course':
            return CourseFactory(school)
        elif factory_name == 'user':
            return UserFactory()
        else:
            raise FactoryTypeError
