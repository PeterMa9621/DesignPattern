from Model.OnlineCourse.OnlineCourseBase import OnlineCourseBase


class Web101(OnlineCourseBase):
    def __init__(self):
        super().__init__(website='https://google.ca/', online_course_name='Google Website 101')
