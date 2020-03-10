class Canada(object):
    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise Exception('Class Canada should be a singleton')
        self.schools = ['University of Alberta', 'University of Calgary']

    @staticmethod
    def get_instance():
        if Canada.__instance is None:
            Canada.__instance = Canada()
        return Canada.__instance

    def get_schools(self):
        return self.schools

    def add_school(self, school):
        self.schools.append(school)
