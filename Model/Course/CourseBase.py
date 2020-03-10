from Interface.Course.CourseInterface import CourseInterface

class CourseBase(CourseInterface):
    def __init__(self):
        self.name = None
        self.code = None
        self.members = []
        self.school = None

    def get_course_name(self):
        return self.name

    def get_course_code(self):
        return self.code

    def get_members(self):
        return self.members

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def get_school(self):
        return self.school

    def set_school(self, school):
        self.school = school

