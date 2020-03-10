from Model.Course.CourseBase import CourseBase
from Model.OnlineCourse.OnlineCourseBase import OnlineCourseBase


class CourseAdapter(object):
    def __init__(self, course_object):
        self.course_object = course_object

    def get_name(self):
        if isinstance(self.course_object, OnlineCourseBase):
            return self.course_object.get_course_name() + ' - ' + self.course_object.get_website()
        elif isinstance(self.course_object, CourseBase):
            return self.course_object.get_course_code() + ' - ' + self.course_object.get_course_name()
        else:
            raise Exception('Course type error')
