from Model.OnlineCourse.OnlineCourseBase import OnlineCourseBase


class Web102(OnlineCourseBase):
    def __init__(self):
        super().__init__(website='https://ualberta.ca/', online_course_name='University of Alberta Website 102')
