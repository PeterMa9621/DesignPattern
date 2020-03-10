from Model.Course.CourseBase import CourseBase

class CMPUT174(CourseBase):
    def __init__(self):
        super().__init__()
        self.name = 'Introduction to the Foundations of Computation I'
        self.code = 'CMPUT174'
        self.members = []
