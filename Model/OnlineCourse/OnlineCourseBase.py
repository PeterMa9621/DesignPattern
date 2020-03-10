from Interface.OnlineCourse.OnlineCourseInterface import OnlineCourseInterface

class OnlineCourseBase(OnlineCourseInterface):
    def __init__(self, website, online_course_name):
        self.website = website
        self.online_course_name = online_course_name

    def get_website(self):
        return self.website

    def get_course_name(self):
        return self.online_course_name
