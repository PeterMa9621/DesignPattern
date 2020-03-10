from Adapter.CourseAdapter.CourseAdapter import CourseAdapter
from Factory.User.UserFactory import UserFactory
from Factory.FactoryProducer import FactoryProducer
from Model.OnlineCourse.Web101 import Web101
from Model.OnlineCourse.Web102 import Web102
from Singleton.Canada import Canada


def factory_demo():
    user_factory = UserFactory()
    student = user_factory.get_instance(instance_type='student', arguments=['A', 1, 'male'])
    tutor = user_factory.get_instance(instance_type='tutor', arguments=['B', 1, 'female'])
    print("I am", student.get_role())
    print("I am", tutor.get_role())

def abstract_factory_demo():
    user_factory = FactoryProducer.get_factory(factory_name='user')
    course_factory = FactoryProducer.get_factory(factory_name='course', school='University of Alberta')
    users_info = [
        ['student', 'Peter', 24, 'male'],
        ['tutor', 'Phoebe', 22, 'female'],
        ['student', 'APerson', 21, 'male']
    ]
    courses_info = ['CMPUT101', 'CMPUT174', 'CMPUT175']
    courses = []
    users = []
    for course_info in courses_info:
        course = course_factory.get_instance(instance_type=course_info, arguments=None)
        print(course.get_course_code() + ' - ' + course.get_course_name(), '| School:', course.get_school())
        courses.append(course)

    print([course.get_school() + ' has ' + course.get_course_code() for course in courses])

    for user_info in users_info:
        user = user_factory.get_instance(instance_type=user_info[0], arguments=user_info[1:])
        print(user.name)
        for course in courses:
            course.add_member(user)
        users.append(user)

    for course in courses:
        print(course.get_school(), course.code + ' - ' + course.name)
        print([member.name + ' is a ' + member.get_role() for member in course.get_members()])
    print([user.name + ' ' + user.gender for user in users])

def singleton_demo():
    canada = Canada.get_instance()
    print(canada.get_schools())
    canada.add_school('UBC')
    print(canada.get_schools())
    canada2 = Canada.get_instance()
    print(canada2.get_schools())

def adapter_demo():
    course_factory = FactoryProducer.get_factory(factory_name='course', school='University of Waterloo')
    course1 = course_factory.get_instance(instance_type='CMPUT101', arguments=None)
    course2 = course_factory.get_instance(instance_type='CMPUT174', arguments=None)
    online_course1 = Web101()
    online_course2 = Web102()

    courses = [course1, course2, online_course1, online_course2]

    for course in courses:
        course_adapter = CourseAdapter(course)
        print(course_adapter.get_name())

def composite_demo():
    user_factory = FactoryProducer.get_factory(factory_name='user')
    tutor_leader = user_factory.get_instance(instance_type='tutor', arguments=['leader', 24, 'female'])
    tutor1 = user_factory.get_instance(instance_type='tutor', arguments=['tutor1', 28, 'male'])
    tutor1_1 = user_factory.get_instance(instance_type='tutor', arguments=['Peter', 21, 'male'])
    tutor1_2 = user_factory.get_instance(instance_type='tutor', arguments=['Phoebe', 24, 'female'])
    tutor2 = user_factory.get_instance(instance_type='tutor', arguments=['tutor2', 18, 'female'])
    tutor1.add_subordinate(tutor1_1)
    tutor1.add_subordinate(tutor1_2)
    tutor_leader.add_subordinate(tutor1)
    tutor_leader.add_subordinate(tutor2)

    print('Tutor leader has subordinates as follows:')
    for subordinate in tutor_leader.get_subordinate():
        if subordinate.has_subordinate():
            for each in subordinate.get_subordinate():
                print(each.name)
        print(subordinate.name)

def main():
    factory_demo()
    abstract_factory_demo()
    singleton_demo()
    adapter_demo()
    composite_demo()

if __name__ == '__main__':
    main()
