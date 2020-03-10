from Model.Course.CourseBase import CourseBase

class CMPUT101(CourseBase):
    def __init__(self):
        super().__init__()
        self.name = 'Introduction to Computing Science'
        self.code = 'CMPUT101'
        self.members = []
