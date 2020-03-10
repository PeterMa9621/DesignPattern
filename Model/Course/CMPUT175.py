from Model.Course.CourseBase import CourseBase

class CMPUT175(CourseBase):
    def __init__(self):
        super().__init__()
        self.name = 'Introduction to the Foundations of Computation II'
        self.code = 'CMPUT175'
        self.members = []
