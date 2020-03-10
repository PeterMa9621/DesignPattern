from AbstractFactory.AbstractFactory import AbstractFactory
from Model.Course.CourseBase import CourseBase
from Model.Course.CMPUT101 import CMPUT101
from Model.Course.CMPUT174 import CMPUT174
from Model.Course.CMPUT175 import CMPUT175

class CourseTypeError(Exception):
    pass

class CourseFactory(AbstractFactory):
    def __init__(self, school):
        self.school = school

    """
        :param course_name: 
        :return: CourseBase
    """
    def get_instance(self, instance_type='CMPUT101', arguments=None) -> CourseBase:

        if instance_type == 'CMPUT101':
            course = CMPUT101()
        elif instance_type == 'CMPUT174':
            course = CMPUT174()
        elif instance_type == 'CMPUT175':
            course = CMPUT175()
        else:
            raise CourseTypeError

        course.set_school(self.school)
        return course
