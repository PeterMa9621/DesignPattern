import abc


class OnlineCourseInterface(object, metaclass=abc.ABCMeta):
    def get_website(self):
        raise NotImplementedError('get_website was not implemented')

    def get_course_name(self):
        raise NotImplementedError('get_online_course_name was not implemented')
